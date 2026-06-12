"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.worker_summary

WorkerSummaries: TypeAlias = list["aws_sdk_deadline.types.worker_summary.WorkerSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSummaries) -> list:
    import aws_sdk_deadline.types.worker_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.worker_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkerSummaries:
    import aws_sdk_deadline.types.worker_summary

    out: WorkerSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.worker_summary.deserialize_json(item))
    return out
