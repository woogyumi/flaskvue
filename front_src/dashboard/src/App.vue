<template>
  <v-app id="inspire">

    <v-app-bar app>
      안녕하세요
      <!-- -->
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      app
      cliped
      mini-variant-width='48'
      :mini-variant='true'
    >
      <v-list dense width="48" style="line-height: 3em;">
        <div class="menu-icon" v-ripple :class="(active_menu == 'search')?'menu-icon-selected':''" @click="doMenuSelect('search')"><v-icon>mdi-magnify</v-icon></div>
        <div class="menu-icon" v-ripple :class="(active_menu == 'table')?'menu-icon-selected':''" @click="doMenuSelect('table')"><v-icon>mdi-table</v-icon></div>
        <div class="menu-icon" v-ripple :class="(active_menu == 'table2')?'menu-icon-selected':''" @click="doMenuSelect('table2')"><v-icon>mdi-table</v-icon></div>
        <div class="menu-icon" v-ripple :class="(active_menu == 'chart')?'menu-icon-selected':''" @click="doMenuSelect('chart')"><v-icon>mdi-chart-line</v-icon></div>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <search-view v-if="active_menu == 'search'"></search-view>
      <table-view v-else-if="active_menu == 'table'"></table-view>
      <table-view2 v-else-if="active_menu == 'table2'"></table-view2>
      <chart-view v-else-if="active_menu == 'chart'"></chart-view>
    </v-main>
  </v-app>
</template>

<script>
import SearchView from './components/search-view';
import ChartView from './components/chart-view';
import TableView from './components/table-view';
import TableView2 from './components/table-view2';

export default {
  name: 'App',
  data: function() {
    return {
      drawer: true,
      active_menu: 'table'
    }
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
  methods: {
    doMenuSelect(menu) {
      this.active_menu = menu;
    }
  },
  components: {
    'search-view': SearchView,
    'chart-view': ChartView,
    'table-view': TableView,
    'table-view2': TableView2
  },
};
</script>

<style scoped>
  .menu-icon {
    text-align: center;
    cursor: pointer;
  }
  .menu-icon:hover {
    background-color: rgba(255, 255, 255, 0.2);
  }
  .menu-icon-selected {
    border-left: white solid 0.1em;
  }
</style>