"""Generated from Smithy shape ``com.amazonaws.managedblockchain#DeleteMemberInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class DeleteMemberInput(TypedDict):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network from which the member is removed.</p>"""
    member_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemberInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMemberInput:
    out: DeleteMemberInput = {}  # type: ignore[typeddict-item]
    return out
