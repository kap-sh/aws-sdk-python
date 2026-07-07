"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.control_identifier
    import aws_sdk_controltower.types.control_operation_status
    import aws_sdk_controltower.types.control_operation_type
    import aws_sdk_controltower.types.operation_identifier
    import aws_sdk_controltower.types.target_identifier
    import aws_sdk_controltower.types.timestamp


class ControlOperationSummary(TypedDict, closed=True):
    operation_type: NotRequired[
        "aws_sdk_controltower.types.control_operation_type.ControlOperationType"
    ]
    """<p>The type of operation.</p>"""
    start_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The time at which a control operation began.</p>"""
    end_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The time at which the control operation was completed.</p>"""
    status: NotRequired[
        "aws_sdk_controltower.types.control_operation_status.ControlOperationStatus"
    ]
    """<p>The status of the specified control operation.</p>"""
    status_message: NotRequired["str"]
    """<p>A speficic message displayed as part of the control status.</p>"""
    operation_identifier: NotRequired[
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The unique identifier of a control operation.</p>"""
    control_identifier: NotRequired[
        "aws_sdk_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The <code>controlIdentifier</code> of a control.</p>"""
    target_identifier: NotRequired[
        "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The unique identifier of the target of a control operation.</p>"""
    enabled_control_identifier: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>The <code>controlIdentifier</code> of an enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationSummary) -> dict:
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


def deserialize_json(data: dict) -> ControlOperationSummary:
    out: ControlOperationSummary = {}  # type: ignore[typeddict-item]
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
