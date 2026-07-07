"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LinkAttributeUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key
    import aws_sdk_clouddirectory.types.link_attribute_action


class LinkAttributeUpdate(TypedDict, closed=True):
    attribute_key: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_key.AttributeKey"
    ]
    """<p>The key of the attribute being updated.</p>"""
    attribute_action: NotRequired[
        "aws_sdk_clouddirectory.types.link_attribute_action.LinkAttributeAction"
    ]
    """<p>The action to perform as part of the attribute update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkAttributeUpdate) -> dict:
    out: dict = {}
    if "attribute_key" in value:
        import aws_sdk_clouddirectory.types.attribute_key

        out["AttributeKey"] = aws_sdk_clouddirectory.types.attribute_key.serialize_json(
            value["attribute_key"]
        )
    if "attribute_action" in value:
        import aws_sdk_clouddirectory.types.link_attribute_action

        out["AttributeAction"] = (
            aws_sdk_clouddirectory.types.link_attribute_action.serialize_json(
                value["attribute_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinkAttributeUpdate:
    out: LinkAttributeUpdate = {}  # type: ignore[typeddict-item]
    if "AttributeKey" in data:
        import aws_sdk_clouddirectory.types.attribute_key

        out["attribute_key"] = (
            aws_sdk_clouddirectory.types.attribute_key.deserialize_json(
                data["AttributeKey"]
            )
        )
    if "AttributeAction" in data:
        import aws_sdk_clouddirectory.types.link_attribute_action

        out["attribute_action"] = (
            aws_sdk_clouddirectory.types.link_attribute_action.deserialize_json(
                data["AttributeAction"]
            )
        )
    return out
