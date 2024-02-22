import type { Site, SocialObjects } from "./types";

export const SITE: Site = {
  website: "https://richiekastl.com", // replace this with your deployed domain
  author: "Richie Kastl",
  desc: "Richie Kastl's Blog",
  title: "Richie Kastl",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerPage: 10,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
};

export const LOCALE = {
  lang: "en", // html lang code. Set this empty and default will be "en"
  langTag: ["en-EN"], // BCP 47 Language Tags. Set this empty [] to use the environment default
} as const;

export const LOGO_IMAGE = {
  enable: false,
  svg: true,
  width: 216,
  height: 46,
};

export const SOCIALS: SocialObjects = [
  {
    name: "Github",
    href: "https://github.com/richiekastl",
    linkTitle: ` ${SITE.title} on Github`,
    active: true,
  },
  {
    name: "LinkedIn",
    href: "https://linkedin.com/in/rck",
    linkTitle: `${SITE.title} on LinkedIn`,
    active: true,
  },
  {
    name: "X",
    href: "https://x.com/richiekastl",
    linkTitle: `${SITE.title} on X`,
    active: true,
  },
  {
    name: "YouTube",
    href: "https://www.youtube.com/@RichieKastl",
    linkTitle: `${SITE.title} on YouTube`,
    active: true,
  },
];
