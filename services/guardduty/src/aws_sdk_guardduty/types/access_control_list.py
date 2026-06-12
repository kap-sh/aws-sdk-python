"""Generated from Smithy shape ``com.amazonaws.guardduty#AccessControlList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean


class AccessControlList(TypedDict):
    allows_public_read_access: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>A value that indicates whether public read access for the bucket is enabled through an Access Control List (ACL).</p>"""
    allows_public_write_access: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>A value that indicates whether public write access for the bucket is enabled through an Access Control List (ACL).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlList) -> dict:
    out: dict = {}
    if "allows_public_read_access" in value:
        out["allowsPublicReadAccess"] = value["allows_public_read_access"]
    if "allows_public_write_access" in value:
        out["allowsPublicWriteAccess"] = value["allows_public_write_access"]
    return out


def deserialize_json(data: dict) -> AccessControlList:
    out: AccessControlList = {}  # type: ignore[typeddict-item]
    if "allowsPublicReadAccess" in data:
        out["allows_public_read_access"] = data["allowsPublicReadAccess"]
    if "allowsPublicWriteAccess" in data:
        out["allows_public_write_access"] = data["allowsPublicWriteAccess"]
    return out
