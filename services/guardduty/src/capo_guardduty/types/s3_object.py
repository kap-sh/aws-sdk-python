"""Generated from Smithy shape ``com.amazonaws.guardduty#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class S3Object(TypedDict, closed=True):
    e_tag: NotRequired["capo_guardduty.types.string.String"]
    """<p>The entity tag is a hash of the Amazon S3 object. The ETag reflects changes only to the contents of an object, and not its metadata.</p>"""
    key: NotRequired["capo_guardduty.types.string.String"]
    """<p>The key of the Amazon S3 object.</p>"""
    version_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version Id of the Amazon S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    if "e_tag" in value:
        out["eTag"] = value["e_tag"]
    if "key" in value:
        out["key"] = value["key"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if "eTag" in data:
        out["e_tag"] = data["eTag"]
    if "key" in data:
        out["key"] = data["key"]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    return out
