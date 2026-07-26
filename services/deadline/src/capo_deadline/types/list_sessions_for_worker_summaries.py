"""Generated from Smithy shape ``com.amazonaws.deadline#ListSessionsForWorkerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.worker_session_summary

ListSessionsForWorkerSummaries: TypeAlias = list[
    "capo_deadline.types.worker_session_summary.WorkerSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsForWorkerSummaries) -> list:
    import capo_deadline.types.worker_session_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.worker_session_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSessionsForWorkerSummaries:
    import capo_deadline.types.worker_session_summary

    out: ListSessionsForWorkerSummaries = []
    for item in data:
        out.append(capo_deadline.types.worker_session_summary.deserialize_json(item))
    return out
