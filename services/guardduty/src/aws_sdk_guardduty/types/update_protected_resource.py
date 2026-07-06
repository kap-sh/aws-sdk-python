"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateProtectedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.update_s3_bucket_resource


class UpdateProtectedResource(TypedDict, closed=True):
    s3_bucket: NotRequired[
        "aws_sdk_guardduty.types.update_s3_bucket_resource.UpdateS3BucketResource"
    ]
    """<p>Information about the protected S3 bucket resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedResource) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        import aws_sdk_guardduty.types.update_s3_bucket_resource

        out["s3Bucket"] = (
            aws_sdk_guardduty.types.update_s3_bucket_resource.serialize_json(
                value["s3_bucket"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateProtectedResource:
    out: UpdateProtectedResource = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        import aws_sdk_guardduty.types.update_s3_bucket_resource

        out["s3_bucket"] = (
            aws_sdk_guardduty.types.update_s3_bucket_resource.deserialize_json(
                data["s3Bucket"]
            )
        )
    return out
