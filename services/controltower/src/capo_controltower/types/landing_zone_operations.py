"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_operation_summary

LandingZoneOperations: TypeAlias = list[
    "capo_controltower.types.landing_zone_operation_summary.LandingZoneOperationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperations) -> list:
    import capo_controltower.types.landing_zone_operation_summary

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.landing_zone_operation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LandingZoneOperations:
    import capo_controltower.types.landing_zone_operation_summary

    out: LandingZoneOperations = []
    for item in data:
        out.append(
            capo_controltower.types.landing_zone_operation_summary.deserialize_json(
                item
            )
        )
    return out
