"""Generated from Smithy shape ``com.amazonaws.deadline#LimitSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.limit_summary

LimitSummaries: TypeAlias = list["capo_deadline.types.limit_summary.LimitSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: LimitSummaries) -> list:
    import capo_deadline.types.limit_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.limit_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LimitSummaries:
    import capo_deadline.types.limit_summary

    out: LimitSummaries = []
    for item in data:
        out.append(capo_deadline.types.limit_summary.deserialize_json(item))
    return out
