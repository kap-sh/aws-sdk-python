"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_status
    import aws_sdk_kinesis_analytics_v2.types.application_version_id


class ApplicationVersionSummary(TypedDict):
    application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The ID of the application version. Managed Service for Apache Flink updates the <code>ApplicationVersionId</code> each time you update the application.</p>"""
    application_status: (
        "aws_sdk_kinesis_analytics_v2.types.application_status.ApplicationStatus"
    )
    """<p>The status of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationVersionSummary) -> dict:
    out: dict = {}
    out["ApplicationVersionId"] = value["application_version_id"]
    import aws_sdk_kinesis_analytics_v2.types.application_status

    out["ApplicationStatus"] = (
        aws_sdk_kinesis_analytics_v2.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationVersionSummary:
    out: ApplicationVersionSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        raise DeserializationError(
            "ApplicationVersionSummary.application_version_id required"
        )
    if "ApplicationStatus" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_status

        out["application_status"] = (
            aws_sdk_kinesis_analytics_v2.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationVersionSummary.application_status required"
        )
    return out
