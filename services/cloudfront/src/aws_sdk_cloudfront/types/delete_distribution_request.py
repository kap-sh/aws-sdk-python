"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteDistributionRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The distribution ID.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteDistributionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteDistributionRequest:
    out: DeleteDistributionRequest = {}  # type: ignore[typeddict-item]
    return out
