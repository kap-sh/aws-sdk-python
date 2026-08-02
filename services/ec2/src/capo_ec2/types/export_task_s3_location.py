"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ExportTaskS3Location(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination Amazon S3 bucket.</p>"""
    s3_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The prefix (logical hierarchy) in the bucket.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTaskS3Location, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "s3_bucket" in value:
        pairs.append((f"{key_prefix}S3Bucket", str(value["s3_bucket"])))
    if "s3_prefix" in value:
        pairs.append((f"{key_prefix}S3Prefix", str(value["s3_prefix"])))


def deserialize_ec2_query(el: Element) -> ExportTaskS3Location:
    out: ExportTaskS3Location = {}  # type: ignore[typeddict-item]
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_prefix = el.find("S3Prefix")
    if child_s3_prefix is not None:
        out["s3_prefix"] = str(child_s3_prefix.text or "")
    return out
