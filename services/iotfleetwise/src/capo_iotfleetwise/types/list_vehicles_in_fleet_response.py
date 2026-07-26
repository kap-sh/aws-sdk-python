"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListVehiclesInFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.vehicles


class ListVehiclesInFleetResponse(TypedDict, closed=True):
    vehicles: NotRequired["capo_iotfleetwise.types.vehicles.vehicles"]
    """<p> A list of vehicles associated with the fleet. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVehiclesInFleetResponse) -> dict:
    out: dict = {}
    if "vehicles" in value:
        import capo_iotfleetwise.types.vehicles

        out["vehicles"] = capo_iotfleetwise.types.vehicles.serialize_aws_json_1_0(
            value["vehicles"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVehiclesInFleetResponse:
    out: ListVehiclesInFleetResponse = {}  # type: ignore[typeddict-item]
    if "vehicles" in data:
        import capo_iotfleetwise.types.vehicles

        out["vehicles"] = capo_iotfleetwise.types.vehicles.deserialize_aws_json_1_0(
            data["vehicles"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
