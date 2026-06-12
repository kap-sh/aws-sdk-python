"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceChatterFeedIncludeFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

SalesforceChatterFeedIncludeFilterType: TypeAlias = Literal[
    "ACTIVE_USER",
    "STANDARD_USER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE_USER",
        "STANDARD_USER",
    )
)


def serialize_aws_json_1_1(value: SalesforceChatterFeedIncludeFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SalesforceChatterFeedIncludeFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SalesforceChatterFeedIncludeFilterType value: {data!r}"
        )
    return cast(SalesforceChatterFeedIncludeFilterType, data)
