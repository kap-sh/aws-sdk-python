"""Generated from Smithy shape ``com.amazonaws.s3control#GetPublicAccessBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id


class GetPublicAccessBlockRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to retrieve.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetPublicAccessBlockRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetPublicAccessBlockRequest:
    out: GetPublicAccessBlockRequest = {}  # type: ignore[typeddict-item]
    return out
