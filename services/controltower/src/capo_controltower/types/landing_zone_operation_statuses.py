"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_operation_status

LandingZoneOperationStatuses: TypeAlias = list[
    "capo_controltower.types.landing_zone_operation_status.LandingZoneOperationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationStatuses) -> list:
    import capo_controltower.types.landing_zone_operation_status

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.landing_zone_operation_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LandingZoneOperationStatuses:
    import capo_controltower.types.landing_zone_operation_status

    out: LandingZoneOperationStatuses = []
    for item in data:
        out.append(
            capo_controltower.types.landing_zone_operation_status.deserialize_json(item)
        )
    return out
