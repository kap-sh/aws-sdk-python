"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baseline_operation_status
    import aws_sdk_controltower.types.baseline_operation_type
    import aws_sdk_controltower.types.operation_identifier
    import aws_sdk_controltower.types.timestamp


class BaselineOperation(TypedDict):
    operation_identifier: NotRequired[
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The identifier of the specified operation.</p>"""
    operation_type: NotRequired[
        "aws_sdk_controltower.types.baseline_operation_type.BaselineOperationType"
    ]
    """<p>An enumerated type (<code>enum</code>) with possible values of <code>ENABLE_BASELINE</code>, <code>DISABLE_BASELINE</code>, <code>UPDATE_ENABLED_BASELINE</code>, or <code>RESET_ENABLED_BASELINE</code>.</p>"""
    status: NotRequired[
        "aws_sdk_controltower.types.baseline_operation_status.BaselineOperationStatus"
    ]
    """<p>An enumerated type (<code>enum</code>) with possible values of <code>SUCCEEDED</code>, <code>FAILED</code>, or <code>IN_PROGRESS</code>.</p>"""
    start_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The start time of the operation, in ISO 8601 format.</p>"""
    end_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The end time of the operation (if applicable), in ISO 8601 format.</p>"""
    status_message: NotRequired["str"]
    """<p>A status message that gives more information about the operation's status, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaselineOperation) -> dict:
    out: dict = {}
    if "operation_identifier" in value:
        out["operationIdentifier"] = value["operation_identifier"]
    if "operation_type" in value:
        import aws_sdk_controltower.types.baseline_operation_type

        out["operationType"] = (
            aws_sdk_controltower.types.baseline_operation_type.serialize_json(
                value["operation_type"]
            )
        )
    if "status" in value:
        import aws_sdk_controltower.types.baseline_operation_status

        out["status"] = (
            aws_sdk_controltower.types.baseline_operation_status.serialize_json(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_controltower.types.timestamp

        out["startTime"] = aws_sdk_controltower.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_controltower.types.timestamp

        out["endTime"] = aws_sdk_controltower.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> BaselineOperation:
    out: BaselineOperation = {}  # type: ignore[typeddict-item]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    if "operationType" in data:
        import aws_sdk_controltower.types.baseline_operation_type

        out["operation_type"] = (
            aws_sdk_controltower.types.baseline_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    if "status" in data:
        import aws_sdk_controltower.types.baseline_operation_status

        out["status"] = (
            aws_sdk_controltower.types.baseline_operation_status.deserialize_json(
                data["status"]
            )
        )
    if "startTime" in data:
        import aws_sdk_controltower.types.timestamp

        out["start_time"] = aws_sdk_controltower.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_controltower.types.timestamp

        out["end_time"] = aws_sdk_controltower.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
