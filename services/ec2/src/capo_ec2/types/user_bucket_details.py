"""Generated from Smithy shape ``com.amazonaws.ec2#UserBucketDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class UserBucketDetails(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon S3 bucket from which the disk image was created.</p>"""
    s3_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The file name of the disk image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UserBucketDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "s3_bucket" in value:
        pairs.append((f"{key_prefix}S3Bucket", str(value["s3_bucket"])))
    if "s3_key" in value:
        pairs.append((f"{key_prefix}S3Key", str(value["s3_key"])))


def deserialize_ec2_query(el: Element) -> UserBucketDetails:
    out: UserBucketDetails = {}  # type: ignore[typeddict-item]
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_key = el.find("S3Key")
    if child_s3_key is not None:
        out["s3_key"] = str(child_s3_key.text or "")
    return out
