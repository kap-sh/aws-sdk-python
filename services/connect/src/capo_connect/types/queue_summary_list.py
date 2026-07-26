"""Generated from Smithy shape ``com.amazonaws.connect#QueueSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.queue_summary

QueueSummaryList: TypeAlias = list["capo_connect.types.queue_summary.QueueSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueSummaryList) -> list:
    import capo_connect.types.queue_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.queue_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueSummaryList:
    import capo_connect.types.queue_summary

    out: QueueSummaryList = []
    for item in data:
        out.append(capo_connect.types.queue_summary.deserialize_json(item))
    return out
