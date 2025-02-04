---
author: Richard Kastl
pubDatetime: 2025-02-04T08:30:00Z
title: Automation
slug: automation
featured: false
tags:
  - Automation
  - Programming
  - AI
description: Automation
---

What I've been doing lately for clients is automating their workflows.

ChatGPT released Operator and it is a game changer, but it requires another AI to control it to be useful, more on that soon. 

Using Operator made me realize that I could automate away a lot of menial tasks that my clients have. 

An example is adding alt descriptions to images on a WordPress site. 

I wrote a script that takes all the images in a WordPress post and adds the alt descriptions to them. 

It does the following:

1. It uses playwright and navigates to the media library
2. Then it clicks on edit on the first image
3. Uploads it to Gemini
4. Gemini generates the alt description
5. Playwright inserts that alt description into the alt text field
6. It clicks on update
7. And then moves onto the next image
