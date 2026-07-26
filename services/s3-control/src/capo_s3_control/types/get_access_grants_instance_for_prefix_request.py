"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessGrantsInstanceForPrefixRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.s3_prefix


class GetAccessGrantsInstanceForPrefixRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that is making this request.</p>"""
    s3_prefix: "capo_s3_control.types.s3_prefix.S3Prefix"
    """<p>The S3 prefix of the access grants that you would like to retrieve.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessGrantsInstanceForPrefixRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAccessGrantsInstanceForPrefixRequest:
    out: GetAccessGrantsInstanceForPrefixRequest = {}  # type: ignore[typeddict-item]
    return out
