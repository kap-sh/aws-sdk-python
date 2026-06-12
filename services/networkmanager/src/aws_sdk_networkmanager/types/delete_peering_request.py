"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeletePeeringRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.peering_id


class DeletePeeringRequest(TypedDict):
    peering_id: "aws_sdk_networkmanager.types.peering_id.PeeringId"
    """<p>The ID of the peering connection to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePeeringRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePeeringRequest:
    out: DeletePeeringRequest = {}  # type: ignore[typeddict-item]
    return out
