"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_detail

ApplicationComponentDetails: TypeAlias = list[
    "capo_migrationhubstrategy.types.application_component_detail.ApplicationComponentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentDetails) -> list:
    import capo_migrationhubstrategy.types.application_component_detail

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.application_component_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApplicationComponentDetails:
    import capo_migrationhubstrategy.types.application_component_detail

    out: ApplicationComponentDetails = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.application_component_detail.deserialize_json(
                item
            )
        )
    return out
