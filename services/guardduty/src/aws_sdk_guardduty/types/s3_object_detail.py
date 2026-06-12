"""Generated from Smithy shape ``com.amazonaws.guardduty#S3ObjectDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class S3ObjectDetail(TypedDict):
    object_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the S3 object.</p>"""
    key: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Key of the S3 object.</p>"""
    e_tag: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The entity tag is a hash of the S3 object. The ETag reflects changes only to the contents of an object, and not its metadata.</p>"""
    hash: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Hash of the threat detected in this finding.</p>"""
    version_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Version ID of the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectDetail) -> dict:
    out: dict = {}
    if "object_arn" in value:
        out["objectArn"] = value["object_arn"]
    if "key" in value:
        out["key"] = value["key"]
    if "e_tag" in value:
        out["eTag"] = value["e_tag"]
    if "hash" in value:
        out["hash"] = value["hash"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3ObjectDetail:
    out: S3ObjectDetail = {}  # type: ignore[typeddict-item]
    if "objectArn" in data:
        out["object_arn"] = data["objectArn"]
    if "key" in data:
        out["key"] = data["key"]
    if "eTag" in data:
        out["e_tag"] = data["eTag"]
    if "hash" in data:
        out["hash"] = data["hash"]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    return out
