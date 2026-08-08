"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class RequestSpotFleetResponse(TypedDict, closed=True):
    spot_fleet_request_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotFleetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{key_prefix}SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )


def deserialize_ec2_query(el: Element) -> RequestSpotFleetResponse:
    out: RequestSpotFleetResponse = {}  # type: ignore[typeddict-item]
    child_spot_fleet_request_id = el.find("spotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    return out
