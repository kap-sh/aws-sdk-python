"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.s3_bucket
    import capo_elastic_beanstalk.types.s3_key


class S3Location(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_elastic_beanstalk.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 bucket where the data is located.</p>"""
    s3_key: NotRequired["capo_elastic_beanstalk.types.s3_key.S3Key"]
    """<p>The Amazon S3 key where the data is located.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: S3Location, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "s3_bucket" in value:
        pairs.append((f"{prefix}.S3Bucket", str(value["s3_bucket"])))
    if "s3_key" in value:
        pairs.append((f"{prefix}.S3Key", str(value["s3_key"])))


def deserialize_query(el: Element) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_key = el.find("S3Key")
    if child_s3_key is not None:
        out["s3_key"] = str(child_s3_key.text or "")
    return out
