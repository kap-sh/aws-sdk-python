"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateKeyGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group
    import aws_sdk_cloudfront.types.string


class UpdateKeyGroupResult(TypedDict, closed=True):
    key_group: NotRequired["aws_sdk_cloudfront.types.key_group.KeyGroup"]
    """<p>The key group that was just updated.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The identifier for this version of the key group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateKeyGroupResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_group" in value:
        import aws_sdk_cloudfront.types.key_group

        aws_sdk_cloudfront.types.key_group.serialize_xml(
            value["key_group"], el, "KeyGroup"
        )


def deserialize_xml(el: Element) -> UpdateKeyGroupResult:
    out: UpdateKeyGroupResult = {}  # type: ignore[typeddict-item]
    child_key_group = el.find("KeyGroup")
    if child_key_group is not None:
        import aws_sdk_cloudfront.types.key_group

        out["key_group"] = aws_sdk_cloudfront.types.key_group.deserialize_xml(
            child_key_group
        )
    return out
