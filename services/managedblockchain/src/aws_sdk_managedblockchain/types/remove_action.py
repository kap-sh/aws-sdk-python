"""Generated from Smithy shape ``com.amazonaws.managedblockchain#RemoveAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class RemoveAction(TypedDict):
    member_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAction) -> dict:
    out: dict = {}
    out["MemberId"] = value["member_id"]
    return out


def deserialize_json(data: dict) -> RemoveAction:
    out: RemoveAction = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    else:
        raise DeserializationError("RemoveAction.member_id required")
    return out
