"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerSearchSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.worker_search_summary

WorkerSearchSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.worker_search_summary.WorkerSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSearchSummaries) -> list:
    import aws_sdk_deadline.types.worker_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.worker_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkerSearchSummaries:
    import aws_sdk_deadline.types.worker_search_summary

    out: WorkerSearchSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.worker_search_summary.deserialize_json(item))
    return out
