"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectAttributeUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_key
    import capo_clouddirectory.types.object_attribute_action


class ObjectAttributeUpdate(TypedDict, closed=True):
    object_attribute_key: NotRequired[
        "capo_clouddirectory.types.attribute_key.AttributeKey"
    ]
    """<p>The key of the attribute being updated.</p>"""
    object_attribute_action: NotRequired[
        "capo_clouddirectory.types.object_attribute_action.ObjectAttributeAction"
    ]
    """<p>The action to perform as part of the attribute update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributeUpdate) -> dict:
    out: dict = {}
    if "object_attribute_key" in value:
        import capo_clouddirectory.types.attribute_key

        out["ObjectAttributeKey"] = (
            capo_clouddirectory.types.attribute_key.serialize_json(
                value["object_attribute_key"]
            )
        )
    if "object_attribute_action" in value:
        import capo_clouddirectory.types.object_attribute_action

        out["ObjectAttributeAction"] = (
            capo_clouddirectory.types.object_attribute_action.serialize_json(
                value["object_attribute_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectAttributeUpdate:
    out: ObjectAttributeUpdate = {}  # type: ignore[typeddict-item]
    if "ObjectAttributeKey" in data:
        import capo_clouddirectory.types.attribute_key

        out["object_attribute_key"] = (
            capo_clouddirectory.types.attribute_key.deserialize_json(
                data["ObjectAttributeKey"]
            )
        )
    if "ObjectAttributeAction" in data:
        import capo_clouddirectory.types.object_attribute_action

        out["object_attribute_action"] = (
            capo_clouddirectory.types.object_attribute_action.deserialize_json(
                data["ObjectAttributeAction"]
            )
        )
    return out
