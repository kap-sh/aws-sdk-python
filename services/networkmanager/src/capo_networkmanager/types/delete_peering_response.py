"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeletePeeringResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.peering


class DeletePeeringResponse(TypedDict, closed=True):
    peering: NotRequired["capo_networkmanager.types.peering.Peering"]
    """<p>Information about a deleted peering connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePeeringResponse) -> dict:
    out: dict = {}
    if "peering" in value:
        import capo_networkmanager.types.peering

        out["Peering"] = capo_networkmanager.types.peering.serialize_json(
            value["peering"]
        )
    return out


def deserialize_json(data: dict) -> DeletePeeringResponse:
    out: DeletePeeringResponse = {}  # type: ignore[typeddict-item]
    if "Peering" in data:
        import capo_networkmanager.types.peering

        out["peering"] = capo_networkmanager.types.peering.deserialize_json(
            data["Peering"]
        )
    return out
