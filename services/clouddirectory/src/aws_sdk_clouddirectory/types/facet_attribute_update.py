"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.facet_attribute
    import aws_sdk_clouddirectory.types.update_action_type


class FacetAttributeUpdate(TypedDict):
    attribute: NotRequired[
        "aws_sdk_clouddirectory.types.facet_attribute.FacetAttribute"
    ]
    """<p>The attribute to update.</p>"""
    action: NotRequired[
        "aws_sdk_clouddirectory.types.update_action_type.UpdateActionType"
    ]
    """<p>The action to perform when updating the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeUpdate) -> dict:
    out: dict = {}
    if "attribute" in value:
        import aws_sdk_clouddirectory.types.facet_attribute

        out["Attribute"] = aws_sdk_clouddirectory.types.facet_attribute.serialize_json(
            value["attribute"]
        )
    if "action" in value:
        import aws_sdk_clouddirectory.types.update_action_type

        out["Action"] = aws_sdk_clouddirectory.types.update_action_type.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> FacetAttributeUpdate:
    out: FacetAttributeUpdate = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_clouddirectory.types.facet_attribute

        out["attribute"] = (
            aws_sdk_clouddirectory.types.facet_attribute.deserialize_json(
                data["Attribute"]
            )
        )
    if "Action" in data:
        import aws_sdk_clouddirectory.types.update_action_type

        out["action"] = (
            aws_sdk_clouddirectory.types.update_action_type.deserialize_json(
                data["Action"]
            )
        )
    return out
