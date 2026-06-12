"""Generated from Smithy shape ``com.amazonaws.s3control#Grantee``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.grantee_identifier
    import aws_sdk_s3_control.types.grantee_type


class Grantee(TypedDict):
    grantee_type: NotRequired["aws_sdk_s3_control.types.grantee_type.GranteeType"]
    """<p>The type of the grantee to which access has been granted. It can be one of the following values:</p> <ul> <li> <p> <code>IAM</code> - An IAM user or role.</p> </li> <li> <p> <code>DIRECTORY_USER</code> - Your corporate directory user. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.</p> </li> <li> <p> <code>DIRECTORY_GROUP</code> - Your corporate directory group. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.</p> </li> </ul>"""
    grantee_identifier: NotRequired[
        "aws_sdk_s3_control.types.grantee_identifier.GranteeIdentifier"
    ]
    """<p>The unique identifier of the <code>Grantee</code>. If the grantee type is <code>IAM</code>, the identifier is the IAM Amazon Resource Name (ARN) of the user or role. If the grantee type is a directory user or group, the identifier is 128-bit universally unique identifier (UUID) in the format <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>. You can obtain this UUID from your Amazon Web Services IAM Identity Center instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Grantee, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "grantee_type" in value:
        import aws_sdk_s3_control.types.grantee_type

        aws_sdk_s3_control.types.grantee_type.serialize_xml(
            value["grantee_type"], el, "GranteeType"
        )
    if "grantee_identifier" in value:
        SubElement(el, "GranteeIdentifier").text = str(value["grantee_identifier"])


def deserialize_xml(el: Element) -> Grantee:
    out: Grantee = {}  # type: ignore[typeddict-item]
    child_grantee_type = el.find("GranteeType")
    if child_grantee_type is not None:
        import aws_sdk_s3_control.types.grantee_type

        out["grantee_type"] = aws_sdk_s3_control.types.grantee_type.deserialize_xml(
            child_grantee_type
        )
    child_grantee_identifier = el.find("GranteeIdentifier")
    if child_grantee_identifier is not None:
        out["grantee_identifier"] = str(child_grantee_identifier.text or "")
    return out
