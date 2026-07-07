"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LinkAttributeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.typed_attribute_value
    import aws_sdk_clouddirectory.types.update_action_type


class LinkAttributeAction(TypedDict, closed=True):
    attribute_action_type: NotRequired[
        "aws_sdk_clouddirectory.types.update_action_type.UpdateActionType"
    ]
    """<p>A type that can be either <code>UPDATE_OR_CREATE</code> or <code>DELETE</code>.</p>"""
    attribute_update_value: NotRequired[
        "aws_sdk_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The value that you want to update to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkAttributeAction) -> dict:
    out: dict = {}
    if "attribute_action_type" in value:
        import aws_sdk_clouddirectory.types.update_action_type

        out["AttributeActionType"] = (
            aws_sdk_clouddirectory.types.update_action_type.serialize_json(
                value["attribute_action_type"]
            )
        )
    if "attribute_update_value" in value:
        import aws_sdk_clouddirectory.types.typed_attribute_value

        out["AttributeUpdateValue"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value.serialize_json(
                value["attribute_update_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinkAttributeAction:
    out: LinkAttributeAction = {}  # type: ignore[typeddict-item]
    if "AttributeActionType" in data:
        import aws_sdk_clouddirectory.types.update_action_type

        out["attribute_action_type"] = (
            aws_sdk_clouddirectory.types.update_action_type.deserialize_json(
                data["AttributeActionType"]
            )
        )
    if "AttributeUpdateValue" in data:
        import aws_sdk_clouddirectory.types.typed_attribute_value

        out["attribute_update_value"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["AttributeUpdateValue"]
            )
        )
    return out
