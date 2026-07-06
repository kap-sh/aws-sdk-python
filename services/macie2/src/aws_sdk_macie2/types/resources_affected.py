"""Generated from Smithy shape ``com.amazonaws.macie2#ResourcesAffected``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.s3_bucket
    import aws_sdk_macie2.types.s3_object


class ResourcesAffected(TypedDict, closed=True):
    s3_bucket: NotRequired["aws_sdk_macie2.types.s3_bucket.S3Bucket"]
    """<p>The details of the S3 bucket that the finding applies to.</p>"""
    s3_object: NotRequired["aws_sdk_macie2.types.s3_object.S3Object"]
    """<p>The details of the S3 object that the finding applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesAffected) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        import aws_sdk_macie2.types.s3_bucket

        out["s3Bucket"] = aws_sdk_macie2.types.s3_bucket.serialize_json(
            value["s3_bucket"]
        )
    if "s3_object" in value:
        import aws_sdk_macie2.types.s3_object

        out["s3Object"] = aws_sdk_macie2.types.s3_object.serialize_json(
            value["s3_object"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesAffected:
    out: ResourcesAffected = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        import aws_sdk_macie2.types.s3_bucket

        out["s3_bucket"] = aws_sdk_macie2.types.s3_bucket.deserialize_json(
            data["s3Bucket"]
        )
    if "s3Object" in data:
        import aws_sdk_macie2.types.s3_object

        out["s3_object"] = aws_sdk_macie2.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    return out
