"""Generated from Smithy shape ``com.amazonaws.deadline#CreateMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.identity_center_application_arn
    import aws_sdk_deadline.types.monitor_id


class CreateMonitorResponse(TypedDict, closed=True):
    monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId"
    """<p>The unique identifier of the monitor.</p>"""
    identity_center_application_arn: "aws_sdk_deadline.types.identity_center_application_arn.IdentityCenterApplicationArn"
    """<p>The Amazon Resource Name that IAM Identity Center assigns to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorResponse) -> dict:
    out: dict = {}
    out["monitorId"] = value["monitor_id"]
    out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    return out


def deserialize_json(data: dict) -> CreateMonitorResponse:
    out: CreateMonitorResponse = {}  # type: ignore[typeddict-item]
    if "monitorId" in data:
        out["monitor_id"] = data["monitorId"]
    else:
        raise DeserializationError("CreateMonitorResponse.monitor_id required")
    if "identityCenterApplicationArn" in data:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    else:
        raise DeserializationError(
            "CreateMonitorResponse.identity_center_application_arn required"
        )
    return out
