"""Generated from Smithy shape ``com.amazonaws.s3control#ListCallerAccessGrantsEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.identity_center_application_arn
    import aws_sdk_s3_control.types.permission
    import aws_sdk_s3_control.types.s3_prefix


class ListCallerAccessGrantsEntry(TypedDict):
    permission: NotRequired["aws_sdk_s3_control.types.permission.Permission"]
    """<p>The type of permission granted, which can be one of the following values:</p> <ul> <li> <p> <code>READ</code> - Grants read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> - Grants write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> - Grants both read and write access to the S3 data.</p> </li> </ul>"""
    grant_scope: NotRequired["aws_sdk_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 path of the data to which you have been granted access. </p>"""
    application_arn: NotRequired[
        "aws_sdk_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListCallerAccessGrantsEntry, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "permission" in value:
        import aws_sdk_s3_control.types.permission

        aws_sdk_s3_control.types.permission.serialize_xml(
            value["permission"], el, "Permission"
        )
    if "grant_scope" in value:
        SubElement(el, "GrantScope").text = str(value["grant_scope"])
    if "application_arn" in value:
        SubElement(el, "ApplicationArn").text = str(value["application_arn"])


def deserialize_xml(el: Element) -> ListCallerAccessGrantsEntry:
    out: ListCallerAccessGrantsEntry = {}  # type: ignore[typeddict-item]
    child_permission = el.find("Permission")
    if child_permission is not None:
        import aws_sdk_s3_control.types.permission

        out["permission"] = aws_sdk_s3_control.types.permission.deserialize_xml(
            child_permission
        )
    child_grant_scope = el.find("GrantScope")
    if child_grant_scope is not None:
        out["grant_scope"] = str(child_grant_scope.text or "")
    child_application_arn = el.find("ApplicationArn")
    if child_application_arn is not None:
        out["application_arn"] = str(child_application_arn.text or "")
    return out
