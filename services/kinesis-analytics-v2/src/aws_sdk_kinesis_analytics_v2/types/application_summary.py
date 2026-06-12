"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_mode
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_status
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.resource_arn
    import aws_sdk_kinesis_analytics_v2.types.runtime_environment


class ApplicationSummary(TypedDict):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of the application.</p>"""
    application_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the application.</p>"""
    application_status: (
        "aws_sdk_kinesis_analytics_v2.types.application_status.ApplicationStatus"
    )
    """<p>The status of the application.</p>"""
    application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>Provides the current application version.</p>"""
    runtime_environment: (
        "aws_sdk_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    )
    """<p>The runtime environment for the application.</p>"""
    application_mode: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_mode.ApplicationMode"
    ]
    """<p>For a Managed Service for Apache Flink application, the mode is <code>STREAMING</code>. For a Managed Service for Apache Flink Studio notebook, it is <code>INTERACTIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["ApplicationARN"] = value["application_arn"]
    import aws_sdk_kinesis_analytics_v2.types.application_status

    out["ApplicationStatus"] = (
        aws_sdk_kinesis_analytics_v2.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    import aws_sdk_kinesis_analytics_v2.types.runtime_environment

    out["RuntimeEnvironment"] = (
        aws_sdk_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
            value["runtime_environment"]
        )
    )
    if "application_mode" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_mode

        out["ApplicationMode"] = (
            aws_sdk_kinesis_analytics_v2.types.application_mode.serialize_aws_json_1_1(
                value["application_mode"]
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
        import aws_sdk_kinesis_analytics_v2.types.application_status

        out["application_status"] = (
            aws_sdk_kinesis_analytics_v2.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        raise DeserializationError("ApplicationSummary.application_status required")
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        raise DeserializationError("ApplicationSummary.application_version_id required")
    if "RuntimeEnvironment" in data:
        import aws_sdk_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            aws_sdk_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    else:
        raise DeserializationError("ApplicationSummary.runtime_environment required")
    if "ApplicationMode" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_mode

        out["application_mode"] = (
            aws_sdk_kinesis_analytics_v2.types.application_mode.deserialize_aws_json_1_1(
                data["ApplicationMode"]
            )
        )
    return out
