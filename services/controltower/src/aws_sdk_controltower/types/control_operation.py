"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.control_identifier
    import aws_sdk_controltower.types.control_operation_status
    import aws_sdk_controltower.types.control_operation_type
    import aws_sdk_controltower.types.operation_identifier
    import aws_sdk_controltower.types.target_identifier
    import aws_sdk_controltower.types.timestamp


class ControlOperation(TypedDict):
    operation_type: NotRequired[
        "aws_sdk_controltower.types.control_operation_type.ControlOperationType"
    ]
    """<p>One of <code>ENABLE_CONTROL</code> or <code>DISABLE_CONTROL</code>.</p>"""
    start_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The time that the operation began.</p>"""
    end_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The time that the operation finished.</p>"""
    status: NotRequired[
        "aws_sdk_controltower.types.control_operation_status.ControlOperationStatus"
    ]
    """<p>One of <code>IN_PROGRESS</code>, <code>SUCEEDED</code>, or <code>FAILED</code>.</p>"""
    status_message: NotRequired["str"]
    """<p>If the operation result is <code>FAILED</code>, this string contains a message explaining why the operation failed.</p>"""
    operation_identifier: NotRequired[
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The identifier of the specified operation.</p>"""
    control_identifier: NotRequired[
        "aws_sdk_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The <code>controlIdentifier</code> of the control for the operation.</p>"""
    target_identifier: NotRequired[
        "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The target upon which the control operation is working.</p>"""
    enabled_control_identifier: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>The <code>controlIdentifier</code> of the enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperation) -> dict:
    out: dict = {}
    if "operation_type" in value:
        import aws_sdk_controltower.types.control_operation_type

        out["operationType"] = (
            aws_sdk_controltower.types.control_operation_type.serialize_json(
                value["operation_type"]
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
    if "status" in value:
        import aws_sdk_controltower.types.control_operation_status

        out["status"] = (
            aws_sdk_controltower.types.control_operation_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "operation_identifier" in value:
        out["operationIdentifier"] = value["operation_identifier"]
    if "control_identifier" in value:
        out["controlIdentifier"] = value["control_identifier"]
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "enabled_control_identifier" in value:
        out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> ControlOperation:
    out: ControlOperation = {}  # type: ignore[typeddict-item]
    if "operationType" in data:
        import aws_sdk_controltower.types.control_operation_type

        out["operation_type"] = (
            aws_sdk_controltower.types.control_operation_type.deserialize_json(
                data["operationType"]
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
    if "status" in data:
        import aws_sdk_controltower.types.control_operation_status

        out["status"] = (
            aws_sdk_controltower.types.control_operation_status.deserialize_json(
                data["status"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    if "controlIdentifier" in data:
        out["control_identifier"] = data["controlIdentifier"]
    if "targetIdentifier" in data:
        out["target_identifier"] = data["targetIdentifier"]
    if "enabledControlIdentifier" in data:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    return out
