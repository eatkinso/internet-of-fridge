DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

/*
contains ALL items that have been scanned in the past
*/

CREATE TABLE global_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  upc INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  item_type TEXT NOT NULL, -- dairy, vegetables, cleaning product, etc (used to sort);
  descr TEXT NOT NULL, -- short description;
  item_state INTEGER NOT NULL, -- new, almost empty, etc;
  item_location TEXT NOT NULL, -- location (ie fridge, laundry, bathroom, etc)
);

