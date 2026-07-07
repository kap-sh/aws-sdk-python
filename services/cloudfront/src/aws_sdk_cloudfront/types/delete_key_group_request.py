"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteKeyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteKeyGroupRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the key group that you are deleting. To get the identifier, use <code>ListKeyGroups</code>.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version of the key group that you are deleting. The version is the key group's <code>ETag</code> value. To get the <code>ETag</code>, use <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteKeyGroupRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteKeyGroupRequest:
    out: DeleteKeyGroupRequest = {}  # type: ignore[typeddict-item]
    return out
