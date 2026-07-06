"""Generated from Smithy shape ``com.amazonaws.guardduty#BucketPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean


class BucketPolicy(TypedDict, closed=True):
    allows_public_read_access: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>A value that indicates whether public read access for the bucket is enabled through a bucket policy.</p>"""
    allows_public_write_access: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>A value that indicates whether public write access for the bucket is enabled through a bucket policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketPolicy) -> dict:
    out: dict = {}
    if "allows_public_read_access" in value:
        out["allowsPublicReadAccess"] = value["allows_public_read_access"]
    if "allows_public_write_access" in value:
        out["allowsPublicWriteAccess"] = value["allows_public_write_access"]
    return out


def deserialize_json(data: dict) -> BucketPolicy:
    out: BucketPolicy = {}  # type: ignore[typeddict-item]
    if "allowsPublicReadAccess" in data:
        out["allows_public_read_access"] = data["allowsPublicReadAccess"]
    if "allowsPublicWriteAccess" in data:
        out["allows_public_write_access"] = data["allowsPublicWriteAccess"]
    return out
