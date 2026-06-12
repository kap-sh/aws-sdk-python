"""Generated from Smithy shape ``com.amazonaws.connect#QueueTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.queue_type

QueueTypes: TypeAlias = list["aws_sdk_connect.types.queue_type.QueueType"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueTypes) -> list:
    import aws_sdk_connect.types.queue_type

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.queue_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueTypes:
    import aws_sdk_connect.types.queue_type

    out: QueueTypes = []
    for item in data:
        out.append(aws_sdk_connect.types.queue_type.deserialize_json(item))
    return out
