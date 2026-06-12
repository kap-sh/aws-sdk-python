"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GroupByAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups_tagging_api.errors import DeserializationError

GroupByAttribute: TypeAlias = Literal[
    "TARGET_ID",
    "REGION",
    "RESOURCE_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TARGET_ID",
        "REGION",
        "RESOURCE_TYPE",
    )
)


def serialize_aws_json_1_1(value: GroupByAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupByAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupByAttribute value: {data!r}")
    return cast(GroupByAttribute, data)
