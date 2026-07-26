"""Generated from Smithy shape ``com.amazonaws.eks#AssociateIdentityProviderConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.tag_map
    import capo_eks.types.update


class AssociateIdentityProviderConfigResponse(TypedDict, closed=True):
    update: NotRequired["capo_eks.types.update.Update"]
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>The tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateIdentityProviderConfigResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.serialize_json(value["update"])
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssociateIdentityProviderConfigResponse:
    out: AssociateIdentityProviderConfigResponse = {}  # type: ignore[typeddict-item]
    if "update" in data:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.deserialize_json(data["update"])
    if "tags" in data:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    return out
