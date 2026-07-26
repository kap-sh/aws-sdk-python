"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.session_action_summary

SessionActionSummaries: TypeAlias = list[
    "capo_deadline.types.session_action_summary.SessionActionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionSummaries) -> list:
    import capo_deadline.types.session_action_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.session_action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionActionSummaries:
    import capo_deadline.types.session_action_summary

    out: SessionActionSummaries = []
    for item in data:
        out.append(capo_deadline.types.session_action_summary.deserialize_json(item))
    return out
