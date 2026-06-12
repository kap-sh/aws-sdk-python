"""Generated from Smithy shape ``com.amazonaws.connect#QueueSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.queue_summary

QueueSummaryList: TypeAlias = list["aws_sdk_connect.types.queue_summary.QueueSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueSummaryList) -> list:
    import aws_sdk_connect.types.queue_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.queue_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueSummaryList:
    import aws_sdk_connect.types.queue_summary

    out: QueueSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.queue_summary.deserialize_json(item))
    return out
