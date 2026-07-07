"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.boolean_object


class DescribeApplicationRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of the application.</p>"""
    include_additional_details: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>Displays verbose information about a Managed Service for Apache Flink application, including the application's job plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "include_additional_details" in value:
        out["IncludeAdditionalDetails"] = value["include_additional_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationRequest:
    out: DescribeApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DescribeApplicationRequest.application_name required"
        )
    if "IncludeAdditionalDetails" in data:
        out["include_additional_details"] = data["IncludeAdditionalDetails"]
    return out
