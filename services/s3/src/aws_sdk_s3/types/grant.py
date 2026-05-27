"""Generated from Smithy shape ``com.amazonaws.s3#Grant``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.grantee
    import aws_sdk_s3.types.permission


class Grant(TypedDict):
    grantee: NotRequired["aws_sdk_s3.types.grantee.Grantee"]
    """<p>The person being granted permissions.</p>"""
    permission: NotRequired["aws_sdk_s3.types.permission.Permission"]
    """<p>Specifies the permission given to the grantee.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Grant, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "grantee" in value:
        import aws_sdk_s3.types.grantee

        aws_sdk_s3.types.grantee.serialize_xml(value["grantee"], el, "Grantee")
    if "permission" in value:
        import aws_sdk_s3.types.permission

        aws_sdk_s3.types.permission.serialize_xml(value["permission"], el, "Permission")


def deserialize_xml(el: Element) -> Grant:
    out: Grant = {}  # type: ignore[typeddict-item]
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import aws_sdk_s3.types.grantee

        out["grantee"] = aws_sdk_s3.types.grantee.deserialize_xml(child_grantee)
    child_permission = el.find("Permission")
    if child_permission is not None:
        import aws_sdk_s3.types.permission

        out["permission"] = aws_sdk_s3.types.permission.deserialize_xml(
            child_permission
        )
    return out
