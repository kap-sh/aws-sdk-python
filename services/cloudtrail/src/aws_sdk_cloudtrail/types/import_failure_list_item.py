"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportFailureListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.import_failure_status
    import aws_sdk_cloudtrail.types.string


class ImportFailureListItem(TypedDict, closed=True):
    location: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p> The location of the failure in the S3 bucket. </p>"""
    status: NotRequired[
        "aws_sdk_cloudtrail.types.import_failure_status.ImportFailureStatus"
    ]
    """<p> The status of the import. </p>"""
    error_type: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p> The type of import error. </p>"""
    error_message: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p> Provides the reason the import failed. </p>"""
    last_updated_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> When the import was last updated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportFailureListItem) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "status" in value:
        import aws_sdk_cloudtrail.types.import_failure_status

        out["Status"] = (
            aws_sdk_cloudtrail.types.import_failure_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "last_updated_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["LastUpdatedTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportFailureListItem:
    out: ImportFailureListItem = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        out["location"] = data["Location"]
    if "Status" in data:
        import aws_sdk_cloudtrail.types.import_failure_status

        out["status"] = (
            aws_sdk_cloudtrail.types.import_failure_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LastUpdatedTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["last_updated_time"] = (
            aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
