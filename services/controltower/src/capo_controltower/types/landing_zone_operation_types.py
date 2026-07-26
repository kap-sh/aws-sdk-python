"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_operation_type

LandingZoneOperationTypes: TypeAlias = list[
    "capo_controltower.types.landing_zone_operation_type.LandingZoneOperationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationTypes) -> list:
    import capo_controltower.types.landing_zone_operation_type

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.landing_zone_operation_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LandingZoneOperationTypes:
    import capo_controltower.types.landing_zone_operation_type

    out: LandingZoneOperationTypes = []
    for item in data:
        out.append(
            capo_controltower.types.landing_zone_operation_type.deserialize_json(item)
        )
    return out
