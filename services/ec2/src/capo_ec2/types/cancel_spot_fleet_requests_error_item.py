"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancel_spot_fleet_requests_error
    import capo_ec2.types.string


class CancelSpotFleetRequestsErrorItem(TypedDict, closed=True):
    error: NotRequired[
        "capo_ec2.types.cancel_spot_fleet_requests_error.CancelSpotFleetRequestsError"
    ]
    """<p>The error.</p>"""
    spot_fleet_request_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsErrorItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "error" in value:
        import capo_ec2.types.cancel_spot_fleet_requests_error

        capo_ec2.types.cancel_spot_fleet_requests_error.serialize_ec2_query(
            value["error"], pairs, f"{key_prefix}Error"
        )
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{key_prefix}SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsErrorItem:
    out: CancelSpotFleetRequestsErrorItem = {}  # type: ignore[typeddict-item]
    child_error = el.find("error")
    if child_error is not None:
        import capo_ec2.types.cancel_spot_fleet_requests_error

        out["error"] = (
            capo_ec2.types.cancel_spot_fleet_requests_error.deserialize_ec2_query(
                child_error
            )
        )
    child_spot_fleet_request_id = el.find("spotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    return out
