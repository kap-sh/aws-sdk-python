"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class RequestSpotFleetResponse(TypedDict):
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotFleetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )


def deserialize_ec2_query(el: Element) -> RequestSpotFleetResponse:
    out: RequestSpotFleetResponse = {}  # type: ignore[typeddict-item]
    child_spot_fleet_request_id = el.find("SpotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    return out
