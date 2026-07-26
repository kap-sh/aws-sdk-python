"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_summary

ExecutionSummaries: TypeAlias = list[
    "capo_iotsitewise.types.execution_summary.ExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaries) -> list:
    import capo_iotsitewise.types.execution_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.execution_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExecutionSummaries:
    import capo_iotsitewise.types.execution_summary

    out: ExecutionSummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.execution_summary.deserialize_json(item))
    return out
