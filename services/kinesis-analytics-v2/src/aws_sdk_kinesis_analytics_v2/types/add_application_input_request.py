"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.input


class AddApplicationInputRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of your existing application to which you want to add the streaming source.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The current version of your application. You must provide the <code>ApplicationVersionID</code> or the <code>ConditionalToken</code>.You can use the <a>DescribeApplication</a> operation to find the current application version.</p>"""
    input: "aws_sdk_kinesis_analytics_v2.types.input.Input"
    """<p>The <a>Input</a> to add.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationInputRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import aws_sdk_kinesis_analytics_v2.types.input

    out["Input"] = aws_sdk_kinesis_analytics_v2.types.input.serialize_aws_json_1_1(
        value["input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationInputRequest:
    out: AddApplicationInputRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "AddApplicationInputRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "AddApplicationInputRequest.current_application_version_id required"
        )
    if "Input" in data:
        import aws_sdk_kinesis_analytics_v2.types.input

        out["input"] = (
            aws_sdk_kinesis_analytics_v2.types.input.deserialize_aws_json_1_1(
                data["Input"]
            )
        )
    else:
        raise DeserializationError("AddApplicationInputRequest.input required")
    return out
