"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectAttributeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_attribute_value
    import capo_clouddirectory.types.update_action_type


class ObjectAttributeAction(TypedDict, closed=True):
    object_attribute_action_type: NotRequired[
        "capo_clouddirectory.types.update_action_type.UpdateActionType"
    ]
    """<p>A type that can be either <code>Update</code> or <code>Delete</code>.</p>"""
    object_attribute_update_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The value that you want to update to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributeAction) -> dict:
    out: dict = {}
    if "object_attribute_action_type" in value:
        import capo_clouddirectory.types.update_action_type

        out["ObjectAttributeActionType"] = (
            capo_clouddirectory.types.update_action_type.serialize_json(
                value["object_attribute_action_type"]
            )
        )
    if "object_attribute_update_value" in value:
        import capo_clouddirectory.types.typed_attribute_value

        out["ObjectAttributeUpdateValue"] = (
            capo_clouddirectory.types.typed_attribute_value.serialize_json(
                value["object_attribute_update_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectAttributeAction:
    out: ObjectAttributeAction = {}  # type: ignore[typeddict-item]
    if "ObjectAttributeActionType" in data:
        import capo_clouddirectory.types.update_action_type

        out["object_attribute_action_type"] = (
            capo_clouddirectory.types.update_action_type.deserialize_json(
                data["ObjectAttributeActionType"]
            )
        )
    if "ObjectAttributeUpdateValue" in data:
        import capo_clouddirectory.types.typed_attribute_value

        out["object_attribute_update_value"] = (
            capo_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["ObjectAttributeUpdateValue"]
            )
        )
    return out
