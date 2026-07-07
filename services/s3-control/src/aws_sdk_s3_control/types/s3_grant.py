"""Generated from Smithy shape ``com.amazonaws.s3control#S3Grant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_grantee
    import aws_sdk_s3_control.types.s3_permission


class S3Grant(TypedDict, closed=True):
    grantee: NotRequired["aws_sdk_s3_control.types.s3_grantee.S3Grantee"]
    """<p></p>"""
    permission: NotRequired["aws_sdk_s3_control.types.s3_permission.S3Permission"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Grant, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "grantee" in value:
        import aws_sdk_s3_control.types.s3_grantee

        aws_sdk_s3_control.types.s3_grantee.serialize_xml(
            value["grantee"], el, "Grantee"
        )
    if "permission" in value:
        import aws_sdk_s3_control.types.s3_permission

        aws_sdk_s3_control.types.s3_permission.serialize_xml(
            value["permission"], el, "Permission"
        )


def deserialize_xml(el: Element) -> S3Grant:
    out: S3Grant = {}  # type: ignore[typeddict-item]
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import aws_sdk_s3_control.types.s3_grantee

        out["grantee"] = aws_sdk_s3_control.types.s3_grantee.deserialize_xml(
            child_grantee
        )
    child_permission = el.find("Permission")
    if child_permission is not None:
        import aws_sdk_s3_control.types.s3_permission

        out["permission"] = aws_sdk_s3_control.types.s3_permission.deserialize_xml(
            child_permission
        )
    return out
