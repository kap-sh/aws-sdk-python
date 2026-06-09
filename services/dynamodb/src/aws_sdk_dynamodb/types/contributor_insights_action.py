"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ContributorInsightsAction: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
    )
)


def serialize_aws_json_1_0(value: ContributorInsightsAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContributorInsightsAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContributorInsightsAction value: {data!r}")
    return cast(ContributorInsightsAction, data)
