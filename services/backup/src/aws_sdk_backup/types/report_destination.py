"""Generated from Smithy shape ``com.amazonaws.backup#ReportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.string_list


class ReportDestination(TypedDict, closed=True):
    s3_bucket_name: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The unique name of the Amazon S3 bucket that receives your reports.</p>"""
    s3_keys: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    """<p>The object key that uniquely identifies your reports in your S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportDestination) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_keys" in value:
        import aws_sdk_backup.types.string_list

        out["S3Keys"] = aws_sdk_backup.types.string_list.serialize_json(
            value["s3_keys"]
        )
    return out


def deserialize_json(data: dict) -> ReportDestination:
    out: ReportDestination = {}  # type: ignore[typeddict-item]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3Keys" in data:
        import aws_sdk_backup.types.string_list

        out["s3_keys"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["S3Keys"]
        )
    return out
