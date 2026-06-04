"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsMode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ContributorInsightsMode: TypeAlias = Literal[
    "ACCESSED_AND_THROTTLED_KEYS",
    "THROTTLED_KEYS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESSED_AND_THROTTLED_KEYS",
        "THROTTLED_KEYS",
    )
)


def serialize_aws_json_1_0(value: ContributorInsightsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContributorInsightsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContributorInsightsMode value: {data!r}")
    return cast(ContributorInsightsMode, data)
