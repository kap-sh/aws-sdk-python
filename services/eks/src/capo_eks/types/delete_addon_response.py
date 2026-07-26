"""Generated from Smithy shape ``com.amazonaws.eks#DeleteAddonResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.addon


class DeleteAddonResponse(TypedDict, closed=True):
    addon: NotRequired["capo_eks.types.addon.Addon"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAddonResponse) -> dict:
    out: dict = {}
    if "addon" in value:
        import capo_eks.types.addon

        out["addon"] = capo_eks.types.addon.serialize_json(value["addon"])
    return out


def deserialize_json(data: dict) -> DeleteAddonResponse:
    out: DeleteAddonResponse = {}  # type: ignore[typeddict-item]
    if "addon" in data:
        import capo_eks.types.addon

        out["addon"] = capo_eks.types.addon.deserialize_json(data["addon"])
    return out
