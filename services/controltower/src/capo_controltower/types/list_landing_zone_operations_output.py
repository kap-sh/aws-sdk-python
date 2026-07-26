"""Generated from Smithy shape ``com.amazonaws.controltower#ListLandingZoneOperationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_operations


class ListLandingZoneOperationsOutput(TypedDict, closed=True):
    landing_zone_operations: (
        "capo_controltower.types.landing_zone_operations.LandingZoneOperations"
    )
    """<p>Lists landing zone operations.</p>"""
    next_token: NotRequired["str"]
    """<p>Retrieves the next page of results. If the string is empty, the response is the end of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLandingZoneOperationsOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.landing_zone_operations

    out["landingZoneOperations"] = (
        capo_controltower.types.landing_zone_operations.serialize_json(
            value["landing_zone_operations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLandingZoneOperationsOutput:
    out: ListLandingZoneOperationsOutput = {}  # type: ignore[typeddict-item]
    if "landingZoneOperations" in data:
        import capo_controltower.types.landing_zone_operations

        out["landing_zone_operations"] = (
            capo_controltower.types.landing_zone_operations.deserialize_json(
                data["landingZoneOperations"]
            )
        )
    else:
        raise DeserializationError(
            "ListLandingZoneOperationsOutput.landing_zone_operations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
