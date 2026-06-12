"""Generated from Smithy shape ``com.amazonaws.controltower#ListLandingZoneOperationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_operation_filter
    import aws_sdk_controltower.types.list_landing_zone_operations_max_results


class ListLandingZoneOperationsInput(TypedDict):
    filter: NotRequired[
        "aws_sdk_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
    ]
    """<p>An input filter for the <code>ListLandingZoneOperations</code> API that lets you select the types of landing zone operations to view.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to continue the list from a previous API call with the same parameters.</p>"""
    max_results: NotRequired[
        "aws_sdk_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
    ]
    """<p>How many results to return per API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLandingZoneOperationsInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_controltower.types.landing_zone_operation_filter

        out["filter"] = (
            aws_sdk_controltower.types.landing_zone_operation_filter.serialize_json(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListLandingZoneOperationsInput:
    out: ListLandingZoneOperationsInput = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_controltower.types.landing_zone_operation_filter

        out["filter"] = (
            aws_sdk_controltower.types.landing_zone_operation_filter.deserialize_json(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
