"""Generated from Smithy shape ``com.amazonaws.s3control#DissociateAccessGrantsIdentityCenterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id


class DissociateAccessGrantsIdentityCenterRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DissociateAccessGrantsIdentityCenterRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DissociateAccessGrantsIdentityCenterRequest:
    out: DissociateAccessGrantsIdentityCenterRequest = {}  # type: ignore[typeddict-item]
    return out
