"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_sap.types.operation_event_status
    import aws_sdk_ssm_sap.types.resource


class OperationEvent(TypedDict, closed=True):
    description: NotRequired["str"]
    r"""<p>A description of the operation event. For example, \"Stop the EC2 instance i-abcdefgh987654321\".</p>"""
    resource: NotRequired["aws_sdk_ssm_sap.types.resource.Resource"]
    """<p>The resource involved in the operations event.</p> <p>Contains <code>ResourceArn</code> ARN and <code>ResourceType</code>.</p>"""
    status: NotRequired[
        "aws_sdk_ssm_sap.types.operation_event_status.OperationEventStatus"
    ]
    """<p>The status of the operation event. The possible statuses are: <code>IN_PROGRESS</code>, <code>COMPLETED</code>, and <code>FAILED</code>.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message relating to a specific operation event.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of the specified operation event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OperationEvent) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "resource" in value:
        import aws_sdk_ssm_sap.types.resource

        out["Resource"] = aws_sdk_ssm_sap.types.resource.serialize_json(
            value["resource"]
        )
    if "status" in value:
        import aws_sdk_ssm_sap.types.operation_event_status

        out["Status"] = aws_sdk_ssm_sap.types.operation_event_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "timestamp" in value:
        import aws_sdk_ssm_sap.types._prelude.timestamp

        out["Timestamp"] = aws_sdk_ssm_sap.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> OperationEvent:
    out: OperationEvent = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Resource" in data:
        import aws_sdk_ssm_sap.types.resource

        out["resource"] = aws_sdk_ssm_sap.types.resource.deserialize_json(
            data["Resource"]
        )
    if "Status" in data:
        import aws_sdk_ssm_sap.types.operation_event_status

        out["status"] = aws_sdk_ssm_sap.types.operation_event_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "Timestamp" in data:
        import aws_sdk_ssm_sap.types._prelude.timestamp

        out["timestamp"] = aws_sdk_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["Timestamp"]
        )
    return out
