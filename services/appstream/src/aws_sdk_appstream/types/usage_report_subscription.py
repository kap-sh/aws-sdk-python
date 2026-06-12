"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportSubscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.last_report_generation_execution_errors
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.timestamp
    import aws_sdk_appstream.types.usage_report_schedule


class UsageReportSubscription(TypedDict):
    s3_bucket_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The Amazon S3 bucket where generated reports are stored.</p> <p>If you enabled on-instance session scripts and Amazon S3 logging for your session script configuration, WorkSpaces Applications created an S3 bucket to store the script output. The bucket is unique to your account and Region. When you enable usage reporting in this case, WorkSpaces Applications uses the same bucket to store your usage reports. If you haven't already enabled on-instance session scripts, when you enable usage reports, WorkSpaces Applications creates a new S3 bucket.</p>"""
    schedule: NotRequired[
        "aws_sdk_appstream.types.usage_report_schedule.UsageReportSchedule"
    ]
    """<p>The schedule for generating usage reports.</p>"""
    last_generated_report_date: NotRequired[
        "aws_sdk_appstream.types.timestamp.Timestamp"
    ]
    """<p>The time when the last usage report was generated.</p>"""
    subscription_errors: NotRequired[
        "aws_sdk_appstream.types.last_report_generation_execution_errors.LastReportGenerationExecutionErrors"
    ]
    """<p>The errors that were returned if usage reports couldn't be generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageReportSubscription) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "schedule" in value:
        import aws_sdk_appstream.types.usage_report_schedule

        out["Schedule"] = (
            aws_sdk_appstream.types.usage_report_schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "last_generated_report_date" in value:
        import aws_sdk_appstream.types.timestamp

        out["LastGeneratedReportDate"] = (
            aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
                value["last_generated_report_date"]
            )
        )
    if "subscription_errors" in value:
        import aws_sdk_appstream.types.last_report_generation_execution_errors

        out["SubscriptionErrors"] = (
            aws_sdk_appstream.types.last_report_generation_execution_errors.serialize_aws_json_1_1(
                value["subscription_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageReportSubscription:
    out: UsageReportSubscription = {}  # type: ignore[typeddict-item]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "Schedule" in data:
        import aws_sdk_appstream.types.usage_report_schedule

        out["schedule"] = (
            aws_sdk_appstream.types.usage_report_schedule.deserialize_aws_json_1_1(
                data["Schedule"]
            )
        )
    if "LastGeneratedReportDate" in data:
        import aws_sdk_appstream.types.timestamp

        out["last_generated_report_date"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["LastGeneratedReportDate"]
            )
        )
    if "SubscriptionErrors" in data:
        import aws_sdk_appstream.types.last_report_generation_execution_errors

        out["subscription_errors"] = (
            aws_sdk_appstream.types.last_report_generation_execution_errors.deserialize_aws_json_1_1(
                data["SubscriptionErrors"]
            )
        )
    return out
