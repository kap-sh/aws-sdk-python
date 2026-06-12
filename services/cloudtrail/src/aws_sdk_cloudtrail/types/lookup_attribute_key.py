"""Generated from Smithy shape ``com.amazonaws.cloudtrail#LookupAttributeKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

LookupAttributeKey: TypeAlias = Literal[
    "EventId",
    "EventName",
    "ReadOnly",
    "Username",
    "ResourceType",
    "ResourceName",
    "EventSource",
    "AccessKeyId",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EventId",
        "EventName",
        "ReadOnly",
        "Username",
        "ResourceType",
        "ResourceName",
        "EventSource",
        "AccessKeyId",
    )
)


def serialize_aws_json_1_1(value: LookupAttributeKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LookupAttributeKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LookupAttributeKey value: {data!r}")
    return cast(LookupAttributeKey, data)
