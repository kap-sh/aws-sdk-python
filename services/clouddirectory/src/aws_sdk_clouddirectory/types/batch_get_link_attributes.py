"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchGetLinkAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name_list
    import aws_sdk_clouddirectory.types.typed_link_specifier


class BatchGetLinkAttributes(TypedDict):
    typed_link_specifier: (
        "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Allows a typed link specifier to be accepted as input.</p>"""
    attribute_names: (
        "aws_sdk_clouddirectory.types.attribute_name_list.AttributeNameList"
    )
    """<p>A list of attribute names whose values will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetLinkAttributes) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.typed_link_specifier

    out["TypedLinkSpecifier"] = (
        aws_sdk_clouddirectory.types.typed_link_specifier.serialize_json(
            value["typed_link_specifier"]
        )
    )
    import aws_sdk_clouddirectory.types.attribute_name_list

    out["AttributeNames"] = (
        aws_sdk_clouddirectory.types.attribute_name_list.serialize_json(
            value["attribute_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetLinkAttributes:
    out: BatchGetLinkAttributes = {}  # type: ignore[typeddict-item]
    if "TypedLinkSpecifier" in data:
        import aws_sdk_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetLinkAttributes.typed_link_specifier required"
        )
    if "AttributeNames" in data:
        import aws_sdk_clouddirectory.types.attribute_name_list

        out["attribute_names"] = (
            aws_sdk_clouddirectory.types.attribute_name_list.deserialize_json(
                data["AttributeNames"]
            )
        )
    else:
        raise DeserializationError("BatchGetLinkAttributes.attribute_names required")
    return out
