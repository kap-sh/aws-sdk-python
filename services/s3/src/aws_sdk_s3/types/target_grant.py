"""Generated from Smithy shape ``com.amazonaws.s3#TargetGrant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_logs_permission
    import aws_sdk_s3.types.grantee


class TargetGrant(TypedDict):
    grantee: NotRequired["aws_sdk_s3.types.grantee.Grantee"]
    """<p>Container for the person being granted permissions.</p>"""
    permission: NotRequired[
        "aws_sdk_s3.types.bucket_logs_permission.BucketLogsPermission"
    ]
    """<p>Logging permissions assigned to the grantee for the bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TargetGrant, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "grantee" in value:
        import aws_sdk_s3.types.grantee

        aws_sdk_s3.types.grantee.serialize_xml(value["grantee"], el, "Grantee")
    if "permission" in value:
        import aws_sdk_s3.types.bucket_logs_permission

        aws_sdk_s3.types.bucket_logs_permission.serialize_xml(
            value["permission"], el, "Permission"
        )


def deserialize_xml(el: Element) -> TargetGrant:
    out: TargetGrant = {}  # type: ignore[typeddict-item]
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import aws_sdk_s3.types.grantee

        out["grantee"] = aws_sdk_s3.types.grantee.deserialize_xml(child_grantee)
    child_permission = el.find("Permission")
    if child_permission is not None:
        import aws_sdk_s3.types.bucket_logs_permission

        out["permission"] = aws_sdk_s3.types.bucket_logs_permission.deserialize_xml(
            child_permission
        )
    return out
