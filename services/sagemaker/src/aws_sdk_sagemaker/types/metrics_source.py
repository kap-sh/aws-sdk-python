"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricsSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.content_digest
    import aws_sdk_sagemaker.types.content_type
    import aws_sdk_sagemaker.types.s3_uri


class MetricsSource(TypedDict, closed=True):
    content_type: NotRequired["aws_sdk_sagemaker.types.content_type.ContentType"]
    """<p>The metric source content type.</p>"""
    content_digest: NotRequired["aws_sdk_sagemaker.types.content_digest.ContentDigest"]
    """<p>The hash key used for the metrics source.</p>"""
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI for the metrics source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsSource) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "content_digest" in value:
        out["ContentDigest"] = value["content_digest"]
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricsSource:
    out: MetricsSource = {}  # type: ignore[typeddict-item]
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "ContentDigest" in data:
        out["content_digest"] = data["ContentDigest"]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
