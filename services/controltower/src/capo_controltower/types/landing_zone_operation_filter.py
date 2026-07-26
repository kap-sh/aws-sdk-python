"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_operation_statuses
    import capo_controltower.types.landing_zone_operation_types


class LandingZoneOperationFilter(TypedDict, closed=True):
    types: NotRequired[
        "capo_controltower.types.landing_zone_operation_types.LandingZoneOperationTypes"
    ]
    """<p>The set of landing zone operation types selected by the filter.</p>"""
    statuses: NotRequired[
        "capo_controltower.types.landing_zone_operation_statuses.LandingZoneOperationStatuses"
    ]
    """<p>The statuses of the set of landing zone operations selected by the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationFilter) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_controltower.types.landing_zone_operation_types

        out["types"] = (
            capo_controltower.types.landing_zone_operation_types.serialize_json(
                value["types"]
            )
        )
    if "statuses" in value:
        import capo_controltower.types.landing_zone_operation_statuses

        out["statuses"] = (
            capo_controltower.types.landing_zone_operation_statuses.serialize_json(
                value["statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> LandingZoneOperationFilter:
    out: LandingZoneOperationFilter = {}  # type: ignore[typeddict-item]
    if "types" in data:
        import capo_controltower.types.landing_zone_operation_types

        out["types"] = (
            capo_controltower.types.landing_zone_operation_types.deserialize_json(
                data["types"]
            )
        )
    if "statuses" in data:
        import capo_controltower.types.landing_zone_operation_statuses

        out["statuses"] = (
            capo_controltower.types.landing_zone_operation_statuses.deserialize_json(
                data["statuses"]
            )
        )
    return out
