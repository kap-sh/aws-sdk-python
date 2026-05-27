"""Generated from Smithy shape ``com.amazonaws.ec2#GroupBy``."""

from typing import Literal, TypeAlias

GroupBy: TypeAlias = Literal[
    "resource-region",
    "availability-zone-id",
    "account-id",
    "account-name",
    "instance-family",
    "instance-type",
    "instance-platform",
    "reservation-arn",
    "reservation-id",
    "reservation-type",
    "reservation-create-timestamp",
    "reservation-start-timestamp",
    "reservation-end-timestamp",
    "reservation-end-date-type",
    "tenancy",
    "reservation-state",
    "reservation-instance-match-criteria",
    "reservation-unused-financial-owner",
]
