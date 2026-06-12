"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyGroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group


class KeyGroupSummary(TypedDict):
    key_group: "aws_sdk_cloudfront.types.key_group.KeyGroup"
    """<p>A key group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyGroupSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.key_group

    aws_sdk_cloudfront.types.key_group.serialize_xml(value["key_group"], el, "KeyGroup")


def deserialize_xml(el: Element) -> KeyGroupSummary:
    out: KeyGroupSummary = {}  # type: ignore[typeddict-item]
    child_key_group = el.find("KeyGroup")
    if child_key_group is not None:
        import aws_sdk_cloudfront.types.key_group

        out["key_group"] = aws_sdk_cloudfront.types.key_group.deserialize_xml(
            child_key_group
        )
    else:
        raise DeserializationError("KeyGroupSummary.key_group required")
    return out
