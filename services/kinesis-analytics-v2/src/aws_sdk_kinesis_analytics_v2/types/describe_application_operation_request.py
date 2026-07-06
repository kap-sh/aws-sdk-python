"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.operation_id


class DescribeApplicationOperationRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    operation_id: "aws_sdk_kinesis_analytics_v2.types.operation_id.OperationId"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationOperationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationOperationRequest:
    out: DescribeApplicationOperationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DescribeApplicationOperationRequest.application_name required"
        )
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError(
            "DescribeApplicationOperationRequest.operation_id required"
        )
    return out
