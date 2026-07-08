# Fikxi - Database Design

## Version

v0.1.0

## Purpose

This document defines the first database design for Fikxi.

Fikxi is a multilingual local services marketplace where customers post jobs, workers submit bids, customers accept bids, jobs get scheduled, and payments are tracked.

---

## Core Database Tables

## 1. users

Stores basic login and account information for all platform users.

A user can be a customer, worker, company user, or admin.

### Fields

- id
- full_name
- phone_number
- email
- password_hash
- role
- preferred_language
- is_active
- created_at
- updated_at

### Roles

- customer
- worker
- company
- admin

### Preferred Languages

- en
- hi
- mr

---

## 2. worker_profiles

Stores extra details for users who register as workers.

### Fields

- id
- user_id
- bio
- years_of_experience
- city
- area
- verification_status
- average_rating
- total_jobs_completed
- created_at
- updated_at

### Verification Statuses

- not_submitted
- pending_review
- verified
- rejected
- suspended

### Relationship

- One user can have one worker profile.

---

## 3. customer_profiles

Stores extra details for users who register as customers.

### Fields

- id
- user_id
- city
- area
- created_at
- updated_at

### Relationship

- One user can have one customer profile.

---

## 4. service_categories

Stores service categories available on Fikxi.

Examples:
- AC Repair and Service
- Electrician
- Plumbing
- Home Repair
- Courier and Local Delivery
- Car Repair
- Car Service

### Fields

- id
- name_en
- name_hi
- name_mr
- description
- is_active
- created_at
- updated_at

---

## 5. worker_skills

Connects workers to the service categories they can perform.

### Fields

- id
- worker_id
- category_id
- created_at

### Relationship

- One worker can have many skills.
- One service category can belong to many workers.

---

## 6. jobs

Stores jobs posted by customers.

### Fields

- id
- customer_id
- category_id
- title
- description
- location_text
- city
- area
- budget_amount
- preferred_date
- preferred_time_start
- preferred_time_end
- status
- accepted_bid_id
- created_at
- updated_at

### Job Statuses

- open
- bidding
- scheduled
- in_progress
- completed
- cancelled
- disputed

### Relationship

- One customer can post many jobs.
- One job belongs to one service category.
- One job can receive many bids.
- One job can have one accepted bid.

---

## 7. bids

Stores bids submitted by workers for jobs.

### Fields

- id
- job_id
- worker_id
- proposed_amount
- message
- available_date
- available_time_start
- available_time_end
- status
- created_at
- updated_at

### Bid Statuses

- pending
- accepted
- rejected
- withdrawn

### Relationship

- One job can have many bids.
- One worker can submit many bids.
- One bid can be accepted for a job.

---

## 8. payments

Tracks payment status for jobs.

For the MVP, this table will only track payment state. Real payment gateway integration will come later.

### Fields

- id
- job_id
- customer_id
- worker_id
- amount
- platform_fee
- worker_payout
- status
- created_at
- updated_at

### Payment Statuses

- not_started
- pending
- held
- released
- refunded
- failed

### Relationship

- One completed job can have one payment record.

---

## 9. reviews

Stores customer reviews for workers after job completion.

### Fields

- id
- job_id
- customer_id
- worker_id
- rating
- comment
- created_at

### Rating

Rating must be between 1 and 5.

### Relationship

- One job can have one review.
- One worker can receive many reviews.
- One customer can write many reviews.

---

## 10. worker_verifications

Stores worker verification submissions.

For MVP, this stores verification status only. Real Aadhaar/PAN verification integration will come later.

### Fields

- id
- worker_id
- document_type
- document_reference
- status
- admin_notes
- submitted_at
- reviewed_at

### Document Types

- aadhaar
- pan
- driving_license
- other

### Verification Statuses

- pending
- approved
- rejected

---

## Main Relationships

### User Relationships

- One user can be a customer.
- One user can be a worker.
- One user can be an admin.
- One worker profile belongs to one user.
- One customer profile belongs to one user.

### Job Relationships

- One customer can create many jobs.
- One job belongs to one customer.
- One job belongs to one category.
- One job can receive many bids.
- One job can have one accepted bid.
- One job can have one payment.
- One job can have one review.

### Worker Relationships

- One worker can have many skills.
- One worker can submit many bids.
- One worker can complete many jobs.
- One worker can receive many reviews.
- One worker can have verification records.

---

## MVP Database Tables

For the first working backend version, we will build these tables first:

1. users
2. worker_profiles
3. customer_profiles
4. service_categories
5. worker_skills
6. jobs
7. bids
8. payments
9. reviews
10. worker_verifications

---

## Future Tables

These can be added after the MVP:

- company_profiles
- company_job_requests
- notifications
- chat_messages
- disputes
- job_attachments
- worker_documents
- audit_logs
- saved_workers
- saved_jobs