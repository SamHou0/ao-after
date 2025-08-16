import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  srcDir: "..\\md",

  title: "苍 After Story 发布站",
  description: "在此找到关于该同人 Gal 的一切",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '主页', link: '/' },
      { text: '下载', link: '/download' },
      { text: '加群交流', link: '/community' }
    ],

    sidebar: [
      {
        text: 'After Story',
        items: [
          { text: '下载', link: '/download' },
          { text: '更新日志', link: '/changelog' },
          { text: '加群交流', link: '/community' }

        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/SamHou0/ao-after' }
    ]
  }
})
