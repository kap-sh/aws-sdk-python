"""Generated from Smithy shape ``com.amazonaws.eks#AssociateIdentityProviderConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.update


class AssociateIdentityProviderConfigResponse(TypedDict, closed=True):
    update: NotRequired["aws_sdk_eks.types.update.Update"]
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>The tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateIdentityProviderConfigResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.serialize_json(value["update"])
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssociateIdentityProviderConfigResponse:
    out: AssociateIdentityProviderConfigResponse = {}  # type: ignore[typeddict-item]
    if "update" in data:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.deserialize_json(data["update"])
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    return out
