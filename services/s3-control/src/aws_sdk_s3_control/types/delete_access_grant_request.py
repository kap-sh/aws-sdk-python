"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteAccessGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_grant_id
    import aws_sdk_s3_control.types.account_id


class DeleteAccessGrantRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    access_grant_id: "aws_sdk_s3_control.types.access_grant_id.AccessGrantId"
    """<p>The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteAccessGrantRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteAccessGrantRequest:
    out: DeleteAccessGrantRequest = {}  # type: ignore[typeddict-item]
    return out
