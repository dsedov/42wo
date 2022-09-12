import Vue from 'vue'
import underscore from 'vue-underscore';
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
Vue.use(underscore);
new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
