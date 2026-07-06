"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessGrantsInstanceResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id


class GetAccessGrantsInstanceResourcePolicyRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessGrantsInstanceResourcePolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAccessGrantsInstanceResourcePolicyRequest:
    out: GetAccessGrantsInstanceResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
