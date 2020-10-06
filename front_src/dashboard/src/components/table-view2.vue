<template>
    <div class="view-main">
        <v-data-table
            :headers="headers"
            :items="rows"
            class="elevation-1"
            style="width: 80%;"
        >
        <template
            v-slot:body="{ items }"
        >
        <tbody>
          <tr
            v-for="row in items"
            :key="row.name"
          >
            <td v-for="{value} in headers" :key="row.name + value">
                <v-edit-dialog
                    :return-value.sync="editing_value"
                    @save="save(row, value)"
                    @open="open(row, value)"
                >
                {{ row[value] }}
                <template v-slot:input>
                    <v-text-field
                    label="Edit"
                    single-line
                    v-model="editing_value"
                    ></v-text-field>
                </template>
                </v-edit-dialog>
            </td>
          </tr>
        </tbody>
      </template>        
        </v-data-table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            editing_value: '',
            headers: [],
            rows: [],      
            rest_base_url: ''      
        }
    },
    methods: {
        async save(row, keyName) {
            let key = row['host'];
            row[keyName] = this.editing_value;
            console.log(row);
            const response = await fetch(`${this.rest_base_url}/rest/table`, {
                method: 'POST', 
                body: JSON.stringify({
                    'key': key,
                    'row': row
                }),
                headers:{
                    'Content-Type': 'application/json'
                }
            });
            const result = await response.json();
            console.log(result);
        },
        open(row, keyName) {
            this.editing_value = row[keyName];
        }
    },
    async created() {
        if (process.env.NODE_ENV == "development") {
            this.rest_base_url = "http://localhost:5000";
        }

        try {
            const response = await fetch(`${this.rest_base_url}/rest/table`);
            const result = await response.json();
            console.log(result);
            for(const f of result.fields) {
                this.headers.push({text: f, value: f});
            }
            this.rows = result.data;
        } catch(e) {
            console.log(e);
        }
    }
}
</script>

<style scoped>
.view-main {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.item-style {
    cursor: pointer;
}
</style>