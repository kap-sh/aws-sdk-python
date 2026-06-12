"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListVehiclesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.vehicle_summaries


class ListVehiclesResponse(TypedDict):
    vehicle_summaries: NotRequired[
        "aws_sdk_iotfleetwise.types.vehicle_summaries.vehicleSummaries"
    ]
    """<p> A list of vehicles and information about them. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVehiclesResponse) -> dict:
    out: dict = {}
    if "vehicle_summaries" in value:
        import aws_sdk_iotfleetwise.types.vehicle_summaries

        out["vehicleSummaries"] = (
            aws_sdk_iotfleetwise.types.vehicle_summaries.serialize_aws_json_1_0(
                value["vehicle_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVehiclesResponse:
    out: ListVehiclesResponse = {}  # type: ignore[typeddict-item]
    if "vehicleSummaries" in data:
        import aws_sdk_iotfleetwise.types.vehicle_summaries

        out["vehicle_summaries"] = (
            aws_sdk_iotfleetwise.types.vehicle_summaries.deserialize_aws_json_1_0(
                data["vehicleSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
