"""Generated from Smithy shape ``com.amazonaws.pcs#QueueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.queue_summary

QueueList: TypeAlias = list["capo_pcs.types.queue_summary.QueueSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueueList) -> list:
    import capo_pcs.types.queue_summary

    out: list = []
    for item in value:
        out.append(capo_pcs.types.queue_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> QueueList:
    import capo_pcs.types.queue_summary

    out: QueueList = []
    for item in data:
        out.append(capo_pcs.types.queue_summary.deserialize_aws_json_1_0(item))
    return out
