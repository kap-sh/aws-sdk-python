"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.application_update
    import aws_sdk_kinesis_analytics.types.application_version_id


class UpdateApplicationRequest(TypedDict):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the Amazon Kinesis Analytics application to update.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>The current application version ID. You can use the <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\">DescribeApplication</a> operation to get this value.</p>"""
    application_update: (
        "aws_sdk_kinesis_analytics.types.application_update.ApplicationUpdate"
    )
    """<p>Describes application updates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import aws_sdk_kinesis_analytics.types.application_update

    out["ApplicationUpdate"] = (
        aws_sdk_kinesis_analytics.types.application_update.serialize_aws_json_1_1(
            value["application_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("UpdateApplicationRequest.application_name required")
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "UpdateApplicationRequest.current_application_version_id required"
        )
    if "ApplicationUpdate" in data:
        import aws_sdk_kinesis_analytics.types.application_update

        out["application_update"] = (
            aws_sdk_kinesis_analytics.types.application_update.deserialize_aws_json_1_1(
                data["ApplicationUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateApplicationRequest.application_update required"
        )
    return out
