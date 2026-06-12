"""Generated from Smithy shape ``com.amazonaws.connect#ReplicationStatusSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.replication_status_summary

ReplicationStatusSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.replication_status_summary.ReplicationStatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatusSummaryList) -> list:
    import aws_sdk_connect.types.replication_status_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.replication_status_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplicationStatusSummaryList:
    import aws_sdk_connect.types.replication_status_summary

    out: ReplicationStatusSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.replication_status_summary.deserialize_json(item)
        )
    return out
