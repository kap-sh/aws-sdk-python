"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateLensShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.share_id


class CreateLensShareOutput(TypedDict, closed=True):
    share_id: NotRequired["capo_wellarchitected.types.share_id.ShareId"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateLensShareOutput) -> dict:
    out: dict = {}
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    return out


def deserialize_json(data: dict) -> CreateLensShareOutput:
    out: CreateLensShareOutput = {}  # type: ignore[typeddict-item]
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    return out
