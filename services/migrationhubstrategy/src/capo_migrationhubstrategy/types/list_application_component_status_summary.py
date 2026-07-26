"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListApplicationComponentStatusSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_status_summary

ListApplicationComponentStatusSummary: TypeAlias = list[
    "capo_migrationhubstrategy.types.application_component_status_summary.ApplicationComponentStatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationComponentStatusSummary) -> list:
    import capo_migrationhubstrategy.types.application_component_status_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.application_component_status_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListApplicationComponentStatusSummary:
    import capo_migrationhubstrategy.types.application_component_status_summary

    out: ListApplicationComponentStatusSummary = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.application_component_status_summary.deserialize_json(
                item
            )
        )
    return out
