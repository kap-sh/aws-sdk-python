"""Generated from Smithy shape ``com.amazonaws.fsx#EventTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.event_type

EventTypes: TypeAlias = list["aws_sdk_fsx.types.event_type.EventType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypes) -> list:
    import aws_sdk_fsx.types.event_type

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.event_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypes:
    import aws_sdk_fsx.types.event_type

    out: EventTypes = []
    for item in data:
        out.append(aws_sdk_fsx.types.event_type.deserialize_aws_json_1_1(item))
    return out
