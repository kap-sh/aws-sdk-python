"""Generated from Smithy shape ``com.amazonaws.s3control#DeletePublicAccessBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id


class DeletePublicAccessBlockRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to remove.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeletePublicAccessBlockRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeletePublicAccessBlockRequest:
    out: DeletePublicAccessBlockRequest = {}  # type: ignore[typeddict-item]
    return out
