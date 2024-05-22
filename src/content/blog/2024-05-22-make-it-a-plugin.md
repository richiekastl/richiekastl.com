---
author: Richard Kastl
pubDatetime: 2024-05-22T10:02:00Z
title: Tiny Plugins
slug: tiny-plugins
featured: false
tags:
  - WordPress
  - WooCommerce
description: Updating this site
---

I was working on a client's site that I inherited and its using WooCommerce reorders. 

Customers can place orders again in their account area. 

The problem was that there wasn't any indication in the admin that orders were reorders. 

I wrote up some code to fix that problem, and instead of adding it to the sites already bloated functions.php, I made it a tiny plugin.

This plugin's only job is to add a note to orders that are reorders. 

Making it a plugin also makes is so that I could port this functionality to the client's other websites easily. 

Also if this functionality ever stops working for some reason, it'll be easy to find the code responsible. 

I'm going to make tiny plugins more often. 