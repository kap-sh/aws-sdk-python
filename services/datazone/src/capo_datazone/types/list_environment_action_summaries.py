"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_action_summary

ListEnvironmentActionSummaries: TypeAlias = list[
    "capo_datazone.types.environment_action_summary.EnvironmentActionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentActionSummaries) -> list:
    import capo_datazone.types.environment_action_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.environment_action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListEnvironmentActionSummaries:
    import capo_datazone.types.environment_action_summary

    out: ListEnvironmentActionSummaries = []
    for item in data:
        out.append(
            capo_datazone.types.environment_action_summary.deserialize_json(item)
        )
    return out
