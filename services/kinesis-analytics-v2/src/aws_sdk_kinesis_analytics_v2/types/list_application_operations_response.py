"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationOperationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_operation_info_list
    import aws_sdk_kinesis_analytics_v2.types.next_token


class ListApplicationOperationsResponse(TypedDict):
    application_operation_info_list: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_operation_info_list.ApplicationOperationInfoList"
    ]
    next_token: NotRequired["aws_sdk_kinesis_analytics_v2.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationOperationsResponse) -> dict:
    out: dict = {}
    if "application_operation_info_list" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_operation_info_list

        out["ApplicationOperationInfoList"] = (
            aws_sdk_kinesis_analytics_v2.types.application_operation_info_list.serialize_aws_json_1_1(
                value["application_operation_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationOperationsResponse:
    out: ListApplicationOperationsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationOperationInfoList" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_operation_info_list

        out["application_operation_info_list"] = (
            aws_sdk_kinesis_analytics_v2.types.application_operation_info_list.deserialize_aws_json_1_1(
                data["ApplicationOperationInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
