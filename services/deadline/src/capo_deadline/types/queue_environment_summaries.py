"""Generated from Smithy shape ``com.amazonaws.deadline#QueueEnvironmentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.queue_environment_summary

QueueEnvironmentSummaries: TypeAlias = list[
    "capo_deadline.types.queue_environment_summary.QueueEnvironmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueEnvironmentSummaries) -> list:
    import capo_deadline.types.queue_environment_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.queue_environment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueEnvironmentSummaries:
    import capo_deadline.types.queue_environment_summary

    out: QueueEnvironmentSummaries = []
    for item in data:
        out.append(capo_deadline.types.queue_environment_summary.deserialize_json(item))
    return out
