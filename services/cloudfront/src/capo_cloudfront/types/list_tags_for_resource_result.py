"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.tags


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: "capo_cloudfront.types.tags.Tags"
    """<p>A complex type that contains zero or more <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTagsForResourceResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.tags

    capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    else:
        raise DeserializationError("ListTagsForResourceResult.tags required")
    return out
