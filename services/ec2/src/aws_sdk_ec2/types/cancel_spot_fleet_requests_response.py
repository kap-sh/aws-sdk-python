"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set


class CancelSpotFleetRequestsResponse(TypedDict):
    successful_fleet_requests: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set.CancelSpotFleetRequestsSuccessSet"
    ]
    """<p>Information about the Spot Fleet requests that are successfully canceled.</p>"""
    unsuccessful_fleet_requests: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set.CancelSpotFleetRequestsErrorSet"
    ]
    """<p>Information about the Spot Fleet requests that are not successfully canceled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful_fleet_requests" in value:
        import aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set

        aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set.serialize_ec2_query(
            value["successful_fleet_requests"],
            pairs,
            f"{prefix}.SuccessfulFleetRequestSet",
        )
    if "unsuccessful_fleet_requests" in value:
        import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set

        aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set.serialize_ec2_query(
            value["unsuccessful_fleet_requests"],
            pairs,
            f"{prefix}.UnsuccessfulFleetRequestSet",
        )


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsResponse:
    out: CancelSpotFleetRequestsResponse = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfulFleetRequestSet") is not None:
        import aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set

        out["successful_fleet_requests"] = (
            aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set.deserialize_ec2_query(
                el, "SuccessfulFleetRequestSet"
            )
        )
    if el.find("UnsuccessfulFleetRequestSet") is not None:
        import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set

        out["unsuccessful_fleet_requests"] = (
            aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set.deserialize_ec2_query(
                el, "UnsuccessfulFleetRequestSet"
            )
        )
    return out
