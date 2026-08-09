"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancel_spot_fleet_requests_error_set
    import capo_ec2.types.cancel_spot_fleet_requests_success_set


class CancelSpotFleetRequestsResponse(TypedDict, closed=True):
    successful_fleet_requests: NotRequired[
        "capo_ec2.types.cancel_spot_fleet_requests_success_set.CancelSpotFleetRequestsSuccessSet"
    ]
    """<p>Information about the Spot Fleet requests that are successfully canceled.</p>"""
    unsuccessful_fleet_requests: NotRequired[
        "capo_ec2.types.cancel_spot_fleet_requests_error_set.CancelSpotFleetRequestsErrorSet"
    ]
    """<p>Information about the Spot Fleet requests that are not successfully canceled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful_fleet_requests" in value:
        import capo_ec2.types.cancel_spot_fleet_requests_success_set

        capo_ec2.types.cancel_spot_fleet_requests_success_set.serialize_ec2_query(
            value["successful_fleet_requests"],
            pairs,
            f"{key_prefix}SuccessfulFleetRequestSet",
        )
    if "unsuccessful_fleet_requests" in value:
        import capo_ec2.types.cancel_spot_fleet_requests_error_set

        capo_ec2.types.cancel_spot_fleet_requests_error_set.serialize_ec2_query(
            value["unsuccessful_fleet_requests"],
            pairs,
            f"{key_prefix}UnsuccessfulFleetRequestSet",
        )


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsResponse:
    out: CancelSpotFleetRequestsResponse = {}  # type: ignore[typeddict-item]
    child_successful_fleet_requests = el.find("successfulFleetRequestSet")
    if child_successful_fleet_requests is not None:
        import capo_ec2.types.cancel_spot_fleet_requests_success_set

        out["successful_fleet_requests"] = (
            capo_ec2.types.cancel_spot_fleet_requests_success_set.deserialize_ec2_query(
                child_successful_fleet_requests
            )
        )
    child_unsuccessful_fleet_requests = el.find("unsuccessfulFleetRequestSet")
    if child_unsuccessful_fleet_requests is not None:
        import capo_ec2.types.cancel_spot_fleet_requests_error_set

        out["unsuccessful_fleet_requests"] = (
            capo_ec2.types.cancel_spot_fleet_requests_error_set.deserialize_ec2_query(
                child_unsuccessful_fleet_requests
            )
        )
    return out
