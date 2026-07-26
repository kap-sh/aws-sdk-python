"""Generated from Smithy shape ``com.amazonaws.m2#LogGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.log_group_summary

LogGroupSummaries: TypeAlias = list["capo_m2.types.log_group_summary.LogGroupSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupSummaries) -> list:
    import capo_m2.types.log_group_summary

    out: list = []
    for item in value:
        out.append(capo_m2.types.log_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogGroupSummaries:
    import capo_m2.types.log_group_summary

    out: LogGroupSummaries = []
    for item in data:
        out.append(capo_m2.types.log_group_summary.deserialize_json(item))
    return out
