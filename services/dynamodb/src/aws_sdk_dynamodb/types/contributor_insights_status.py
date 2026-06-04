"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ContributorInsightsStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: ContributorInsightsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContributorInsightsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContributorInsightsStatus value: {data!r}")
    return cast(ContributorInsightsStatus, data)
