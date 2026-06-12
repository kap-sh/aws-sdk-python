"""Generated from Smithy shape ``com.amazonaws.connect#QueueSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.queue

QueueSearchSummaryList: TypeAlias = list["aws_sdk_connect.types.queue.Queue"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueSearchSummaryList) -> list:
    import aws_sdk_connect.types.queue

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.queue.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueSearchSummaryList:
    import aws_sdk_connect.types.queue

    out: QueueSearchSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.queue.deserialize_json(item))
    return out
