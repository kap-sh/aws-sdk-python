"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListApplicationComponentSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_summary

ListApplicationComponentSummary: TypeAlias = list[
    "capo_migrationhubstrategy.types.application_component_summary.ApplicationComponentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationComponentSummary) -> list:
    import capo_migrationhubstrategy.types.application_component_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.application_component_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListApplicationComponentSummary:
    import capo_migrationhubstrategy.types.application_component_summary

    out: ListApplicationComponentSummary = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.application_component_summary.deserialize_json(
                item
            )
        )
    return out
