"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceStandardObjectName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: SalesforceStandardObjectName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SalesforceStandardObjectName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SalesforceStandardObjectName value: {data!r}"
        )
    return cast(SalesforceStandardObjectName, data)
