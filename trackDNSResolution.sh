#!/bin/bash
DNS_SERVER="8.8.8.8"
DOMAIN="example.com"
dig @$DNS_SERVER $DOMAIN +stats | grep "Query time"