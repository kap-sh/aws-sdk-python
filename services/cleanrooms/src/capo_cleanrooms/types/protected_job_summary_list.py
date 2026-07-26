"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_summary

ProtectedJobSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.protected_job_summary.ProtectedJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobSummaryList) -> list:
    import capo_cleanrooms.types.protected_job_summary

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.protected_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtectedJobSummaryList:
    import capo_cleanrooms.types.protected_job_summary

    out: ProtectedJobSummaryList = []
    for item in data:
        out.append(capo_cleanrooms.types.protected_job_summary.deserialize_json(item))
    return out
