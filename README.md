# BellBites: food before the bell

> IEEE (XIM CHAPTER) -> TechTank contest prototype

**The problem:** you have 20 minutes between classes, ₹60 in your pocket, and a canteen queue that takes longer than your syllabus.

**The idea:** BellBites tells you what you can actually eat *before the bell rings*. You enter your budget and how long until your next class. It then sorts the canteen by what fits your time and money, including the queue, and lets you order ahead.

Built for the IEEE Day TechTank contest, where it won.



P.S.: This is an updated version where we implemented all the ideas we planned to add. 

To see the prototype which won the Contest, check the bellbite.html file.



## What it does

**For students**

* Asks for your budget and the minutes left before your next class.
* A live countdown to your next class sits at the top right.
* Shows 22 canteen items (icons, ratings, prices) and hides what you can't afford.
* Every item says whether you'll make it back in time, and why: *"12 min queue + 7 min to make"*.
* Sort by best match, price, rating or fastest to make.
* A "Smart pick" suggests the best-rated food and drink that fit your time and budget.
* Budget is tracked across orders, so a second order for a friend uses what is left.
* Pay by UPI or at the counter (both simulated), then get a token with a pickup countdown.
* "My orders" keeps every token until it is collected. Everything survives a refresh.
* An alert (banner, beep, vibration) when the shopkeeper marks your order ready.
* When class starts, the app says your break is over and stops suggesting food.

**Premium (₹99 a month, down from ₹249 for first-time users)**

* A priority lane that skips the long queue and gets orders made first.
* A random "Want food fast?" nudge, plus a Premium button that is always in the header.

**For the shopkeeper**

* A manager screen behind a login (link at the bottom of the page).
* Live list of incoming orders, Premium first, with **Mark ready** and **Collected** buttons.
* Stats for orders waiting, orders ready and the current queue wait.
* Switch items to **Sold out**. Students see it immediately.
* A **Reset demo data** button.

## Try it

Open `index.html` in any browser. There is nothing to install and it works offline, on laptop and phone.

**Manager login (prototype only):** username `admin`, password `123456`

To see both sides together, open the page in two tabs of the same browser: order in one, then open the manager screen in the other and mark the order ready.

## How it works

* Plain HTML, CSS and JavaScript in a single file. No frameworks, no libraries, no network calls.
* Queue time is calculated from the orders currently in the kitchen (Premium orders count first), plus a simulated walk-in crowd.
* Orders, stock and student data are saved in the browser's `localStorage`, which is how the student and manager screens talk to each other.
* A Content Security Policy blocks all outside scripts and connections. Stored data is validated every time it is loaded.
* Accessibility: keyboard use, focus kept inside pop-ups, labelled controls, readable contrast. The axe accessibility scan reported no violations.

## Prototype limits (please read)

* **Not a real system.** Payments, the walk-in queue and the login are all simulated.
* **One browser only.** The student and manager screens share data only inside the same browser, so two different phones cannot see each other's orders.
* **The login is not secure.** The username and password are visible in the page source. A real version needs a server-side login with hashed passwords.

## Editing the code

The security policy is tied to the exact JavaScript in the file. After you edit the JavaScript, run:

```
python3 update_csp.py index.html
```

If you skip this step, the browser refuses to run the script and the page stays blank. Changes to the HTML or CSS don't need it.

## Ideas for next

Future Ideas that were in discussions, but we skipped as it's not implemented in real life.

* A small backend (for example Firebase) so different phones share orders in real time.
* Real payments through a payment gateway.
* Predicting queue time from real order history.
* Server-side manager login.
* Student ratings after collecting an order.

## Credits

Built by Soubhik Raj Ghosh and Kabir Kamran Hossain Mollick.
