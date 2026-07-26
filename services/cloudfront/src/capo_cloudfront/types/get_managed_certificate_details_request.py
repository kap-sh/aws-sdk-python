"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetManagedCertificateDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetManagedCertificateDetailsRequest(TypedDict, closed=True):
    identifier: "capo_cloudfront.types.string.string"
    """<p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetManagedCertificateDetailsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetManagedCertificateDetailsRequest:
    out: GetManagedCertificateDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
