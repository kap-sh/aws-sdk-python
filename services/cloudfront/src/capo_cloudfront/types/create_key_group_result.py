"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateKeyGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_group
    import capo_cloudfront.types.string


class CreateKeyGroupResult(TypedDict, closed=True):
    key_group: NotRequired["capo_cloudfront.types.key_group.KeyGroup"]
    """<p>The key group that was just created.</p>"""
    location: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The URL of the key group.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The identifier for this version of the key group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateKeyGroupResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_group" in value:
        import capo_cloudfront.types.key_group

        capo_cloudfront.types.key_group.serialize_xml(
            value["key_group"], el, "KeyGroup"
        )


def deserialize_xml(el: Element) -> CreateKeyGroupResult:
    out: CreateKeyGroupResult = {}  # type: ignore[typeddict-item]
    child_key_group = el.find("KeyGroup")
    if child_key_group is not None:
        import capo_cloudfront.types.key_group

        out["key_group"] = capo_cloudfront.types.key_group.deserialize_xml(
            child_key_group
        )
    return out
