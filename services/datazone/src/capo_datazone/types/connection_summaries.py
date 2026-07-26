"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.connection_summary

ConnectionSummaries: TypeAlias = list[
    "capo_datazone.types.connection_summary.ConnectionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionSummaries) -> list:
    import capo_datazone.types.connection_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.connection_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectionSummaries:
    import capo_datazone.types.connection_summary

    out: ConnectionSummaries = []
    for item in data:
        out.append(capo_datazone.types.connection_summary.deserialize_json(item))
    return out
