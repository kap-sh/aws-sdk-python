"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceStandardObjectName``."""

from typing import Literal, TypeAlias, cast

SalesforceStandardObjectName: TypeAlias = Literal[
    "ACCOUNT",
    "CAMPAIGN",
    "CASE",
    "CONTACT",
    "CONTRACT",
    "DOCUMENT",
    "GROUP",
    "IDEA",
    "LEAD",
    "OPPORTUNITY",
    "PARTNER",
    "PRICEBOOK",
    "PRODUCT",
    "PROFILE",
    "SOLUTION",
    "TASK",
    "USER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceStandardObjectName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SalesforceStandardObjectName:
    return cast(SalesforceStandardObjectName, data)
