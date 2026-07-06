"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#SourceS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.s3_bucket
    import aws_sdk_applicationcostprofiler.types.s3_bucket_region
    import aws_sdk_applicationcostprofiler.types.s3_key


class SourceS3Location(TypedDict, closed=True):
    bucket: "aws_sdk_applicationcostprofiler.types.s3_bucket.S3Bucket"
    """<p>Name of the bucket.</p>"""
    key: "aws_sdk_applicationcostprofiler.types.s3_key.S3Key"
    """<p>Key of the object.</p>"""
    region: NotRequired[
        "aws_sdk_applicationcostprofiler.types.s3_bucket_region.S3BucketRegion"
    ]
    r"""<p>Region of the bucket. Only required for Regions that are disabled by default. For more infomration about Regions that are disabled by default, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable\"> Enabling a Region</a> in the <i>AWS General Reference guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceS3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "region" in value:
        import aws_sdk_applicationcostprofiler.types.s3_bucket_region

        out["region"] = (
            aws_sdk_applicationcostprofiler.types.s3_bucket_region.serialize_json(
                value["region"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceS3Location:
    out: SourceS3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("SourceS3Location.bucket required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("SourceS3Location.key required")
    if "region" in data:
        import aws_sdk_applicationcostprofiler.types.s3_bucket_region

        out["region"] = (
            aws_sdk_applicationcostprofiler.types.s3_bucket_region.deserialize_json(
                data["region"]
            )
        )
    return out
