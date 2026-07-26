"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetMemberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.resource_id_string


class GetMemberInput(TypedDict, closed=True):
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network to which the member belongs.</p>"""
    member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMemberInput:
    out: GetMemberInput = {}  # type: ignore[typeddict-item]
    return out
