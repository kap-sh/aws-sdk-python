"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AdditionalResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.additional_resource_type
    import capo_wellarchitected.types.urls


class AdditionalResources(TypedDict, closed=True):
    type: NotRequired[
        "capo_wellarchitected.types.additional_resource_type.AdditionalResourceType"
    ]
    """<p>Type of additional resource for a custom lens.</p>"""
    content: NotRequired["capo_wellarchitected.types.urls.Urls"]
    """<p>The URLs for additional resources, either helpful resources or improvement plans, for a custom lens. Up to five additional URLs can be specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResources) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_wellarchitected.types.additional_resource_type

        out["Type"] = (
            capo_wellarchitected.types.additional_resource_type.serialize_json(
                value["type"]
            )
        )
    if "content" in value:
        import capo_wellarchitected.types.urls

        out["Content"] = capo_wellarchitected.types.urls.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> AdditionalResources:
    out: AdditionalResources = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_wellarchitected.types.additional_resource_type

        out["type"] = (
            capo_wellarchitected.types.additional_resource_type.deserialize_json(
                data["Type"]
            )
        )
    if "Content" in data:
        import capo_wellarchitected.types.urls

        out["content"] = capo_wellarchitected.types.urls.deserialize_json(
            data["Content"]
        )
    return out
