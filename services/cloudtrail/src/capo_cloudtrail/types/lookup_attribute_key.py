"""Generated from Smithy shape ``com.amazonaws.cloudtrail#LookupAttributeKey``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: LookupAttributeKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LookupAttributeKey:
    return cast(LookupAttributeKey, data)
