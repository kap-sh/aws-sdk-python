"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationInputProcessingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.id


class DeleteApplicationInputProcessingConfigurationRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of the application.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The application version. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>"""
    input_id: "aws_sdk_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the <a>DescribeApplication</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationInputProcessingConfigurationRequest,
) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["InputId"] = value["input_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationInputProcessingConfigurationRequest:
    out: DeleteApplicationInputProcessingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationInputProcessingConfigurationRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationInputProcessingConfigurationRequest.current_application_version_id required"
        )
    if "InputId" in data:
        out["input_id"] = data["InputId"]
    else:
        raise DeserializationError(
            "DeleteApplicationInputProcessingConfigurationRequest.input_id required"
        )
    return out
