"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectAttributeUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key
    import aws_sdk_clouddirectory.types.object_attribute_action


class ObjectAttributeUpdate(TypedDict):
    object_attribute_key: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_key.AttributeKey"
    ]
    """<p>The key of the attribute being updated.</p>"""
    object_attribute_action: NotRequired[
        "aws_sdk_clouddirectory.types.object_attribute_action.ObjectAttributeAction"
    ]
    """<p>The action to perform as part of the attribute update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributeUpdate) -> dict:
    out: dict = {}
    if "object_attribute_key" in value:
        import aws_sdk_clouddirectory.types.attribute_key

        out["ObjectAttributeKey"] = (
            aws_sdk_clouddirectory.types.attribute_key.serialize_json(
                value["object_attribute_key"]
            )
        )
    if "object_attribute_action" in value:
        import aws_sdk_clouddirectory.types.object_attribute_action

        out["ObjectAttributeAction"] = (
            aws_sdk_clouddirectory.types.object_attribute_action.serialize_json(
                value["object_attribute_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectAttributeUpdate:
    out: ObjectAttributeUpdate = {}  # type: ignore[typeddict-item]
    if "ObjectAttributeKey" in data:
        import aws_sdk_clouddirectory.types.attribute_key

        out["object_attribute_key"] = (
            aws_sdk_clouddirectory.types.attribute_key.deserialize_json(
                data["ObjectAttributeKey"]
            )
        )
    if "ObjectAttributeAction" in data:
        import aws_sdk_clouddirectory.types.object_attribute_action

        out["object_attribute_action"] = (
            aws_sdk_clouddirectory.types.object_attribute_action.deserialize_json(
                data["ObjectAttributeAction"]
            )
        )
    return out
