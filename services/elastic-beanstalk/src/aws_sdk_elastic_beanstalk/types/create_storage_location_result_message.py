"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateStorageLocationResultMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.s3_bucket


class CreateStorageLocationResultMessage(TypedDict, closed=True):
    s3_bucket: NotRequired["aws_sdk_elastic_beanstalk.types.s3_bucket.S3Bucket"]
    """<p>The name of the Amazon S3 bucket created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateStorageLocationResultMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "s3_bucket" in value:
        pairs.append((f"{prefix}.S3Bucket", str(value["s3_bucket"])))


def deserialize_query(el: Element) -> CreateStorageLocationResultMessage:
    out: CreateStorageLocationResultMessage = {}  # type: ignore[typeddict-item]
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    return out
