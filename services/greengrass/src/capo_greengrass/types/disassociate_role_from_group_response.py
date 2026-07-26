"""Generated from Smithy shape ``com.amazonaws.greengrass#DisassociateRoleFromGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class DisassociateRoleFromGroupResponse(TypedDict, closed=True):
    disassociated_at: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the role was disassociated from the group."""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateRoleFromGroupResponse) -> dict:
    out: dict = {}
    if "disassociated_at" in value:
        out["DisassociatedAt"] = value["disassociated_at"]
    return out


def deserialize_json(data: dict) -> DisassociateRoleFromGroupResponse:
    out: DisassociateRoleFromGroupResponse = {}  # type: ignore[typeddict-item]
    if "DisassociatedAt" in data:
        out["disassociated_at"] = data["DisassociatedAt"]
    return out
