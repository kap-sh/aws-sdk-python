"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAllocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.capacity_allocation_status
    import aws_sdk_athena.types.string
    import aws_sdk_athena.types.timestamp


class CapacityAllocation(TypedDict):
    status: "aws_sdk_athena.types.capacity_allocation_status.CapacityAllocationStatus"
    """<p>The status of the capacity allocation.</p>"""
    status_message: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>The status message of the capacity allocation.</p>"""
    request_time: "aws_sdk_athena.types.timestamp.Timestamp"
    """<p>The time when the capacity allocation was requested.</p>"""
    request_completion_time: NotRequired["aws_sdk_athena.types.timestamp.Timestamp"]
    """<p>The time when the capacity allocation request was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAllocation) -> dict:
    out: dict = {}
    import aws_sdk_athena.types.capacity_allocation_status

    out["Status"] = (
        aws_sdk_athena.types.capacity_allocation_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    import aws_sdk_athena.types.timestamp

    out["RequestTime"] = aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
        value["request_time"]
    )
    if "request_completion_time" in value:
        import aws_sdk_athena.types.timestamp

        out["RequestCompletionTime"] = (
            aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
                value["request_completion_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityAllocation:
    out: CapacityAllocation = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_athena.types.capacity_allocation_status

        out["status"] = (
            aws_sdk_athena.types.capacity_allocation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CapacityAllocation.status required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "RequestTime" in data:
        import aws_sdk_athena.types.timestamp

        out["request_time"] = aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
            data["RequestTime"]
        )
    else:
        raise DeserializationError("CapacityAllocation.request_time required")
    if "RequestCompletionTime" in data:
        import aws_sdk_athena.types.timestamp

        out["request_completion_time"] = (
            aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
                data["RequestCompletionTime"]
            )
        )
    return out
