"""Generated from Smithy shape ``com.amazonaws.eks#AssociateEncryptionConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.update


class AssociateEncryptionConfigResponse(TypedDict, closed=True):
    update: NotRequired["capo_eks.types.update.Update"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEncryptionConfigResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.serialize_json(value["update"])
    return out


def deserialize_json(data: dict) -> AssociateEncryptionConfigResponse:
    out: AssociateEncryptionConfigResponse = {}  # type: ignore[typeddict-item]
    if "update" in data:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.deserialize_json(data["update"])
    return out
