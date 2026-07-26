"""Generated from Smithy shape ``com.amazonaws.configservice#EventSource``."""

from typing import Literal, TypeAlias, cast

EventSource: TypeAlias = Literal["aws.config",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSource:
    return cast(EventSource, data)
