"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationOperationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.operation
    import capo_kinesis_analytics_v2.types.operation_id
    import capo_kinesis_analytics_v2.types.operation_status
    import capo_kinesis_analytics_v2.types.timestamp


class ApplicationOperationInfo(TypedDict, closed=True):
    operation: NotRequired["capo_kinesis_analytics_v2.types.operation.Operation"]
    operation_id: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    start_time: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the operation was created.</p>"""
    end_time: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the operation finished.</p>"""
    operation_status: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_status.OperationStatus"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationOperationInfo) -> dict:
    out: dict = {}
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    if "start_time" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["StartTime"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["EndTime"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "operation_status" in value:
        import capo_kinesis_analytics_v2.types.operation_status

        out["OperationStatus"] = (
            capo_kinesis_analytics_v2.types.operation_status.serialize_aws_json_1_1(
                value["operation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationOperationInfo:
    out: ApplicationOperationInfo = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    if "StartTime" in data:
        import capo_kinesis_analytics_v2.types.timestamp

        out["start_time"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import capo_kinesis_analytics_v2.types.timestamp

        out["end_time"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "OperationStatus" in data:
        import capo_kinesis_analytics_v2.types.operation_status

        out["operation_status"] = (
            capo_kinesis_analytics_v2.types.operation_status.deserialize_aws_json_1_1(
                data["OperationStatus"]
            )
        )
    return out
