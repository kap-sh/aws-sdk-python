"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ApplicationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.application_status
    import aws_sdk_kinesis_analytics.types.resource_arn


class ApplicationSummary(TypedDict):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application.</p>"""
    application_arn: "aws_sdk_kinesis_analytics.types.resource_arn.ResourceARN"
    """<p>ARN of the application.</p>"""
    application_status: (
        "aws_sdk_kinesis_analytics.types.application_status.ApplicationStatus"
    )
    """<p>Status of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["ApplicationARN"] = value["application_arn"]
    import aws_sdk_kinesis_analytics.types.application_status

    out["ApplicationStatus"] = (
        aws_sdk_kinesis_analytics.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("ApplicationSummary.application_name required")
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    else:
        raise DeserializationError("ApplicationSummary.application_arn required")
    if "ApplicationStatus" in data:
        import aws_sdk_kinesis_analytics.types.application_status

        out["application_status"] = (
            aws_sdk_kinesis_analytics.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        raise DeserializationError("ApplicationSummary.application_status required")
    return out
