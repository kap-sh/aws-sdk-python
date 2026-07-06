"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.list_application_operations_input_limit
    import aws_sdk_kinesis_analytics_v2.types.next_token
    import aws_sdk_kinesis_analytics_v2.types.operation
    import aws_sdk_kinesis_analytics_v2.types.operation_status


class ListApplicationOperationsRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    limit: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.list_application_operations_input_limit.ListApplicationOperationsInputLimit"
    ]
    next_token: NotRequired["aws_sdk_kinesis_analytics_v2.types.next_token.NextToken"]
    operation: NotRequired["aws_sdk_kinesis_analytics_v2.types.operation.Operation"]
    operation_status: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.operation_status.OperationStatus"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationOperationsRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "operation_status" in value:
        import aws_sdk_kinesis_analytics_v2.types.operation_status

        out["OperationStatus"] = (
            aws_sdk_kinesis_analytics_v2.types.operation_status.serialize_aws_json_1_1(
                value["operation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationOperationsRequest:
    out: ListApplicationOperationsRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "ListApplicationOperationsRequest.application_name required"
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    if "OperationStatus" in data:
        import aws_sdk_kinesis_analytics_v2.types.operation_status

        out["operation_status"] = (
            aws_sdk_kinesis_analytics_v2.types.operation_status.deserialize_aws_json_1_1(
                data["OperationStatus"]
            )
        )
    return out
