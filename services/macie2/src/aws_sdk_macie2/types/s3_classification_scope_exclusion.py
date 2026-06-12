"""Generated from Smithy shape ``com.amazonaws.macie2#S3ClassificationScopeExclusion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_s3_bucket_name


class S3ClassificationScopeExclusion(TypedDict):
    bucket_names: NotRequired[
        "aws_sdk_macie2.types.__list_of_s3_bucket_name.__listOfS3BucketName"
    ]
    """<p>An array of strings, one for each S3 bucket that is excluded. Each string is the full name of an excluded bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ClassificationScopeExclusion) -> dict:
    out: dict = {}
    if "bucket_names" in value:
        import aws_sdk_macie2.types.__list_of_s3_bucket_name

        out["bucketNames"] = (
            aws_sdk_macie2.types.__list_of_s3_bucket_name.serialize_json(
                value["bucket_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3ClassificationScopeExclusion:
    out: S3ClassificationScopeExclusion = {}  # type: ignore[typeddict-item]
    if "bucketNames" in data:
        import aws_sdk_macie2.types.__list_of_s3_bucket_name

        out["bucket_names"] = (
            aws_sdk_macie2.types.__list_of_s3_bucket_name.deserialize_json(
                data["bucketNames"]
            )
        )
    return out
