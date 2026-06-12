"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListFleetsForVehicleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.fleets
    import aws_sdk_iotfleetwise.types.next_token


class ListFleetsForVehicleResponse(TypedDict):
    fleets: NotRequired["aws_sdk_iotfleetwise.types.fleets.fleets"]
    """<p> A list of fleet IDs that the vehicle is associated with. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFleetsForVehicleResponse) -> dict:
    out: dict = {}
    if "fleets" in value:
        import aws_sdk_iotfleetwise.types.fleets

        out["fleets"] = aws_sdk_iotfleetwise.types.fleets.serialize_aws_json_1_0(
            value["fleets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFleetsForVehicleResponse:
    out: ListFleetsForVehicleResponse = {}  # type: ignore[typeddict-item]
    if "fleets" in data:
        import aws_sdk_iotfleetwise.types.fleets

        out["fleets"] = aws_sdk_iotfleetwise.types.fleets.deserialize_aws_json_1_0(
            data["fleets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
