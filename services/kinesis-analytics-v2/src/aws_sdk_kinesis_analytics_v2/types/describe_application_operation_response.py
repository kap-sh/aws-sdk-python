"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_operation_info_details


class DescribeApplicationOperationResponse(TypedDict, closed=True):
    application_operation_info_details: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_operation_info_details.ApplicationOperationInfoDetails"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationOperationResponse) -> dict:
    out: dict = {}
    if "application_operation_info_details" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_operation_info_details

        out["ApplicationOperationInfoDetails"] = (
            aws_sdk_kinesis_analytics_v2.types.application_operation_info_details.serialize_aws_json_1_1(
                value["application_operation_info_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationOperationResponse:
    out: DescribeApplicationOperationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationOperationInfoDetails" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_operation_info_details

        out["application_operation_info_details"] = (
            aws_sdk_kinesis_analytics_v2.types.application_operation_info_details.deserialize_aws_json_1_1(
                data["ApplicationOperationInfoDetails"]
            )
        )
    return out
