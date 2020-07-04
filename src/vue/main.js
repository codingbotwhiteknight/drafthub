import Vue from 'vue';
import Buefy from 'buefy'
import searchform from './components/searchform.vue';
import heading1 from './components/heading1.vue';
import draftarticle from './components/draftarticle.vue';
import coverpreview from './components/coverpreview.vue';
import markdownpreview from './components/markdownpreview.vue';
import inputtags from './components/inputtags.vue';

Vue.use(Buefy);

window.vm = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  components: {
    'searchform': searchform,
    'heading1': heading1,
    'draftarticle': draftarticle,
    'coverpreview': coverpreview,
    'markdownpreview': markdownpreview,
    'inputtags': inputtags,
  },
  data: {
    newArticle: {
      apiTags: [],
      tags: [],
      url: '',
      image: '',
      title: '',
      description: '',
      formError: {
        tags: true,
        url: true,
        image: true,
        title: true,
        description: true,
      }
    },
  },
})