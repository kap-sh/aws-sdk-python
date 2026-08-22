"""Generated from Smithy shape ``com.amazonaws.s3#TargetGrant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_logs_permission
    import capo_s3.types.grantee


class TargetGrant(TypedDict, closed=True):
    grantee: NotRequired["capo_s3.types.grantee.Grantee"]
    """<p>Container for the person being granted permissions.</p>"""
    permission: NotRequired["capo_s3.types.bucket_logs_permission.BucketLogsPermission"]
    """<p>Logging permissions assigned to the grantee for the bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TargetGrant, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "grantee" in value:
        import capo_s3.types.grantee

        capo_s3.types.grantee.serialize_xml(value["grantee"], el, "Grantee")
        el[-1].set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    if "permission" in value:
        import capo_s3.types.bucket_logs_permission

        capo_s3.types.bucket_logs_permission.serialize_xml(
            value["permission"], el, "Permission"
        )


def deserialize_xml(el: Element) -> TargetGrant:
    out: TargetGrant = {}  # type: ignore[typeddict-item]
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import capo_s3.types.grantee

        out["grantee"] = capo_s3.types.grantee.deserialize_xml(child_grantee)
    child_permission = el.find("Permission")
    if child_permission is not None:
        import capo_s3.types.bucket_logs_permission

        out["permission"] = capo_s3.types.bucket_logs_permission.deserialize_xml(
            child_permission
        )
    return out
