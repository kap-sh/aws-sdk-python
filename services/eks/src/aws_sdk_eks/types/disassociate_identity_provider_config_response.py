"""Generated from Smithy shape ``com.amazonaws.eks#DisassociateIdentityProviderConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.update


class DisassociateIdentityProviderConfigResponse(TypedDict):
    update: NotRequired["aws_sdk_eks.types.update.Update"]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateIdentityProviderConfigResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.serialize_json(value["update"])
    return out


def deserialize_json(data: dict) -> DisassociateIdentityProviderConfigResponse:
    out: DisassociateIdentityProviderConfigResponse = {}  # type: ignore[typeddict-item]
    if "update" in data:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.deserialize_json(data["update"])
    return out
