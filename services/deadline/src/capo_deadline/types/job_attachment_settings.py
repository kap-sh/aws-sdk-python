"""Generated from Smithy shape ``com.amazonaws.deadline#JobAttachmentSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.s3_bucket_name
    import capo_deadline.types.s3_prefix


class JobAttachmentSettings(TypedDict, closed=True):
    s3_bucket_name: "capo_deadline.types.s3_bucket_name.S3BucketName"
    """<p>The Amazon S3 bucket name.</p>"""
    root_prefix: "capo_deadline.types.s3_prefix.S3Prefix"
    """<p>The root prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobAttachmentSettings) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["rootPrefix"] = value["root_prefix"]
    return out


def deserialize_json(data: dict) -> JobAttachmentSettings:
    out: JobAttachmentSettings = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        raise DeserializationError("JobAttachmentSettings.s3_bucket_name required")
    if "rootPrefix" in data:
        out["root_prefix"] = data["rootPrefix"]
    else:
        raise DeserializationError("JobAttachmentSettings.root_prefix required")
    return out
