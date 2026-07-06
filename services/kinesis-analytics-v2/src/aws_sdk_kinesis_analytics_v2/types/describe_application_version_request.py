"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_version_id


class DescribeApplicationVersionRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of the application for which you want to get the version description.</p>"""
    application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The ID of the application version for which you want to get the description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationVersionRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["ApplicationVersionId"] = value["application_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationVersionRequest:
    out: DescribeApplicationVersionRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DescribeApplicationVersionRequest.application_name required"
        )
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        raise DeserializationError(
            "DescribeApplicationVersionRequest.application_version_id required"
        )
    return out
