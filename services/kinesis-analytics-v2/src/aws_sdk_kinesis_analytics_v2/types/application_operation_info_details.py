"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationOperationInfoDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_change_details
    import aws_sdk_kinesis_analytics_v2.types.operation
    import aws_sdk_kinesis_analytics_v2.types.operation_failure_details
    import aws_sdk_kinesis_analytics_v2.types.operation_status
    import aws_sdk_kinesis_analytics_v2.types.timestamp


class ApplicationOperationInfoDetails(TypedDict):
    operation: "aws_sdk_kinesis_analytics_v2.types.operation.Operation"
    start_time: "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The timestamp that indicates when the operation was created.</p>"""
    end_time: "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The timestamp that indicates when the operation finished.</p>"""
    operation_status: (
        "aws_sdk_kinesis_analytics_v2.types.operation_status.OperationStatus"
    )
    application_version_change_details: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_change_details.ApplicationVersionChangeDetails"
    ]
    operation_failure_details: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.operation_failure_details.OperationFailureDetails"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationOperationInfoDetails) -> dict:
    out: dict = {}
    out["Operation"] = value["operation"]
    import aws_sdk_kinesis_analytics_v2.types.timestamp

    out["StartTime"] = (
        aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    )
    import aws_sdk_kinesis_analytics_v2.types.timestamp

    out["EndTime"] = (
        aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    )
    import aws_sdk_kinesis_analytics_v2.types.operation_status

    out["OperationStatus"] = (
        aws_sdk_kinesis_analytics_v2.types.operation_status.serialize_aws_json_1_1(
            value["operation_status"]
        )
    )
    if "application_version_change_details" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_version_change_details

        out["ApplicationVersionChangeDetails"] = (
            aws_sdk_kinesis_analytics_v2.types.application_version_change_details.serialize_aws_json_1_1(
                value["application_version_change_details"]
            )
        )
    if "operation_failure_details" in value:
        import aws_sdk_kinesis_analytics_v2.types.operation_failure_details

        out["OperationFailureDetails"] = (
            aws_sdk_kinesis_analytics_v2.types.operation_failure_details.serialize_aws_json_1_1(
                value["operation_failure_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationOperationInfoDetails:
    out: ApplicationOperationInfoDetails = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    else:
        raise DeserializationError("ApplicationOperationInfoDetails.operation required")
    if "StartTime" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["start_time"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationOperationInfoDetails.start_time required"
        )
    if "EndTime" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["end_time"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ApplicationOperationInfoDetails.end_time required")
    if "OperationStatus" in data:
        import aws_sdk_kinesis_analytics_v2.types.operation_status

        out["operation_status"] = (
            aws_sdk_kinesis_analytics_v2.types.operation_status.deserialize_aws_json_1_1(
                data["OperationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationOperationInfoDetails.operation_status required"
        )
    if "ApplicationVersionChangeDetails" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_version_change_details

        out["application_version_change_details"] = (
            aws_sdk_kinesis_analytics_v2.types.application_version_change_details.deserialize_aws_json_1_1(
                data["ApplicationVersionChangeDetails"]
            )
        )
    if "OperationFailureDetails" in data:
        import aws_sdk_kinesis_analytics_v2.types.operation_failure_details

        out["operation_failure_details"] = (
            aws_sdk_kinesis_analytics_v2.types.operation_failure_details.deserialize_aws_json_1_1(
                data["OperationFailureDetails"]
            )
        )
    return out
