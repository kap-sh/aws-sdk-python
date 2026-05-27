"""Generated from Smithy shape ``com.amazonaws.eks#CreateAddonResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon


class CreateAddonResponse(TypedDict):
    addon: NotRequired["aws_sdk_eks.types.addon.Addon"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAddonResponse) -> dict:
    out: dict = {}
    if "addon" in value:
        import aws_sdk_eks.types.addon

        out["addon"] = aws_sdk_eks.types.addon.serialize_json(value["addon"])
    return out


def deserialize_json(data: dict) -> CreateAddonResponse:
    out: CreateAddonResponse = {}  # type: ignore[typeddict-item]
    if "addon" in data:
        import aws_sdk_eks.types.addon

        out["addon"] = aws_sdk_eks.types.addon.deserialize_json(data["addon"])
    return out
