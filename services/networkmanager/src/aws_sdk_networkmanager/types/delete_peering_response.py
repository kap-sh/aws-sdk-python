"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeletePeeringResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.peering


class DeletePeeringResponse(TypedDict, closed=True):
    peering: NotRequired["aws_sdk_networkmanager.types.peering.Peering"]
    """<p>Information about a deleted peering connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePeeringResponse) -> dict:
    out: dict = {}
    if "peering" in value:
        import aws_sdk_networkmanager.types.peering

        out["Peering"] = aws_sdk_networkmanager.types.peering.serialize_json(
            value["peering"]
        )
    return out


def deserialize_json(data: dict) -> DeletePeeringResponse:
    out: DeletePeeringResponse = {}  # type: ignore[typeddict-item]
    if "Peering" in data:
        import aws_sdk_networkmanager.types.peering

        out["peering"] = aws_sdk_networkmanager.types.peering.deserialize_json(
            data["Peering"]
        )
    return out
