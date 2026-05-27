"""Generated from Smithy shape ``com.amazonaws.s3#OwnershipControlsRule``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_ownership


class OwnershipControlsRule(TypedDict):
    object_ownership: "aws_sdk_s3.types.object_ownership.ObjectOwnership"


# --- restXml ser/de ---
def serialize_xml(value: OwnershipControlsRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.object_ownership

    aws_sdk_s3.types.object_ownership.serialize_xml(
        value["object_ownership"], el, "ObjectOwnership"
    )


def deserialize_xml(el: Element) -> OwnershipControlsRule:
    out: OwnershipControlsRule = {}  # type: ignore[typeddict-item]
    child_object_ownership = el.find("ObjectOwnership")
    if child_object_ownership is not None:
        import aws_sdk_s3.types.object_ownership

        out["object_ownership"] = aws_sdk_s3.types.object_ownership.deserialize_xml(
            child_object_ownership
        )
    else:
        raise DeserializationError("OwnershipControlsRule.object_ownership required")
    return out
