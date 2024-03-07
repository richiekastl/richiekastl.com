---
author: Richard Kastl
pubDatetime: 2024-03-07T06:48:00Z
title: Learning Astro
slug: learning-astro
featured: false
tags:
  - Programming
  - Astro
description: Updating this site
---

Yesterday I updated this website to show the entire post on the homepage and on the all posts page, ala Seth Godin's site. 

It took me way to long to figure out. 

The posts astro component used a Card component to show the posts and I couldn't figure out how to pass the post content into it. 

In Astro, the blog uses <a href="https://docs.astro.build/en/guides/content-collections/">content collections</a>. 

In order to grab the content of a post, you must use a promise that returns an Astro component, at least that's how I understand it. 

I don't believe you can pass an entire Astro component into a TSX component, which Card was. 

So I ended up stripping out the card component and transferring the markup to the posts Astro component itself. 

If you're interested in that, you can see the commit here: https://github.com/richiekastl/richiekastl.com/commit/d05bb9c31af4d8b6cb43249ffb6c4b448d432fed

I also changed Twitter to X, because you know, that's a thing. 