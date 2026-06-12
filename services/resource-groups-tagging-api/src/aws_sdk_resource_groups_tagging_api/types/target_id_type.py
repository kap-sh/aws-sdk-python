"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TargetIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups_tagging_api.errors import DeserializationError

TargetIdType: TypeAlias = Literal[
    "ACCOUNT",
    "OU",
    "ROOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "OU",
        "ROOT",
    )
)


def serialize_aws_json_1_1(value: TargetIdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetIdType value: {data!r}")
    return cast(TargetIdType, data)
