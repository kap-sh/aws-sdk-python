"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateMemberOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.resource_id_string


class CreateMemberOutput(TypedDict, closed=True):
    member_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemberOutput) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    return out


def deserialize_json(data: dict) -> CreateMemberOutput:
    out: CreateMemberOutput = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    return out
