"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetKeyGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group
    import aws_sdk_cloudfront.types.string


class GetKeyGroupResult(TypedDict):
    key_group: NotRequired["aws_sdk_cloudfront.types.key_group.KeyGroup"]
    """<p>The key group.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The identifier for this version of the key group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetKeyGroupResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_group" in value:
        import aws_sdk_cloudfront.types.key_group

        aws_sdk_cloudfront.types.key_group.serialize_xml(
            value["key_group"], el, "KeyGroup"
        )


def deserialize_xml(el: Element) -> GetKeyGroupResult:
    out: GetKeyGroupResult = {}  # type: ignore[typeddict-item]
    child_key_group = el.find("KeyGroup")
    if child_key_group is not None:
        import aws_sdk_cloudfront.types.key_group

        out["key_group"] = aws_sdk_cloudfront.types.key_group.deserialize_xml(
            child_key_group
        )
    return out
