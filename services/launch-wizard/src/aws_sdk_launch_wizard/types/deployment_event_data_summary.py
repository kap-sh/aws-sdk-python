"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentEventDataSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_launch_wizard.types.event_status


class DeploymentEventDataSummary(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the deployment event.</p>"""
    description: NotRequired["str"]
    """<p>The description of the deployment event.</p>"""
    status: NotRequired["aws_sdk_launch_wizard.types.event_status.EventStatus"]
    """<p>The status of the deployment event.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason of the deployment event status.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of the deployment event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentEventDataSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_launch_wizard.types.event_status

        out["status"] = aws_sdk_launch_wizard.types.event_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "timestamp" in value:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.serialize_json(
                value["timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentEventDataSummary:
    out: DeploymentEventDataSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_launch_wizard.types.event_status

        out["status"] = aws_sdk_launch_wizard.types.event_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "timestamp" in data:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    return out
