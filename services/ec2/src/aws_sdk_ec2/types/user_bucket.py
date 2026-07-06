"""Generated from Smithy shape ``com.amazonaws.ec2#UserBucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class UserBucket(TypedDict, closed=True):
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket where the disk image is located.</p>"""
    s3_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The file name of the disk image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UserBucket, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "s3_bucket" in value:
        pairs.append((f"{prefix}.S3Bucket", str(value["s3_bucket"])))
    if "s3_key" in value:
        pairs.append((f"{prefix}.S3Key", str(value["s3_key"])))


def deserialize_ec2_query(el: Element) -> UserBucket:
    out: UserBucket = {}  # type: ignore[typeddict-item]
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_key = el.find("S3Key")
    if child_s3_key is not None:
        out["s3_key"] = str(child_s3_key.text or "")
    return out
