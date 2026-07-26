"""Generated from Smithy shape ``com.amazonaws.backup#ReportDeliveryChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.format_list
    import capo_backup.types.string


class ReportDeliveryChannel(TypedDict, closed=True):
    s3_bucket_name: "capo_backup.types.string.string"
    """<p>The unique name of the S3 bucket that receives your reports.</p>"""
    s3_key_prefix: NotRequired["capo_backup.types.string.string"]
    """<p>The prefix for where Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/<code>prefix</code>/Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.</p>"""
    formats: NotRequired["capo_backup.types.format_list.FormatList"]
    """<p>The format of your reports: <code>CSV</code>, <code>JSON</code>, or both. If not specified, the default format is <code>CSV</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportDeliveryChannel) -> dict:
    out: dict = {}
    out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    if "formats" in value:
        import capo_backup.types.format_list

        out["Formats"] = capo_backup.types.format_list.serialize_json(value["formats"])
    return out


def deserialize_json(data: dict) -> ReportDeliveryChannel:
    out: ReportDeliveryChannel = {}  # type: ignore[typeddict-item]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError("ReportDeliveryChannel.s3_bucket_name required")
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if "Formats" in data:
        import capo_backup.types.format_list

        out["formats"] = capo_backup.types.format_list.deserialize_json(data["Formats"])
    return out
