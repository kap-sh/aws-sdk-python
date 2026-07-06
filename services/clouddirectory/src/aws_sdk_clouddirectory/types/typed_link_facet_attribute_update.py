"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkFacetAttributeUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition
    import aws_sdk_clouddirectory.types.update_action_type


class TypedLinkFacetAttributeUpdate(TypedDict, closed=True):
    attribute: "aws_sdk_clouddirectory.types.typed_link_attribute_definition.TypedLinkAttributeDefinition"
    """<p>The attribute to update.</p>"""
    action: "aws_sdk_clouddirectory.types.update_action_type.UpdateActionType"
    """<p>The action to perform when updating the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkFacetAttributeUpdate) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition

    out["Attribute"] = (
        aws_sdk_clouddirectory.types.typed_link_attribute_definition.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_clouddirectory.types.update_action_type

    out["Action"] = aws_sdk_clouddirectory.types.update_action_type.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> TypedLinkFacetAttributeUpdate:
    out: TypedLinkFacetAttributeUpdate = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_clouddirectory.types.typed_link_attribute_definition

        out["attribute"] = (
            aws_sdk_clouddirectory.types.typed_link_attribute_definition.deserialize_json(
                data["Attribute"]
            )
        )
    else:
        raise DeserializationError("TypedLinkFacetAttributeUpdate.attribute required")
    if "Action" in data:
        import aws_sdk_clouddirectory.types.update_action_type

        out["action"] = (
            aws_sdk_clouddirectory.types.update_action_type.deserialize_json(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("TypedLinkFacetAttributeUpdate.action required")
    return out
