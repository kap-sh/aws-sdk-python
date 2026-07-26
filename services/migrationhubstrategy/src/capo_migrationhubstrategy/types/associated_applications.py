"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssociatedApplications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.associated_application

AssociatedApplications: TypeAlias = list[
    "capo_migrationhubstrategy.types.associated_application.AssociatedApplication"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedApplications) -> list:
    import capo_migrationhubstrategy.types.associated_application

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.associated_application.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedApplications:
    import capo_migrationhubstrategy.types.associated_application

    out: AssociatedApplications = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.associated_application.deserialize_json(
                item
            )
        )
    return out
