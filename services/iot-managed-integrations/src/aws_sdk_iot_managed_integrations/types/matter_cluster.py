"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.cluster_id
    import aws_sdk_iot_managed_integrations.types.matter_attributes
    import aws_sdk_iot_managed_integrations.types.matter_commands
    import aws_sdk_iot_managed_integrations.types.matter_events


class MatterCluster(TypedDict):
    id: NotRequired["aws_sdk_iot_managed_integrations.types.cluster_id.ClusterId"]
    """<p>The cluster id.</p>"""
    attributes: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_attributes.MatterAttributes"
    ]
    """<p>The Matter attributes.</p>"""
    commands: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_commands.MatterCommands"
    ]
    """<p>Describe the Matter commands with the Matter command identifier mapped to the command fields.</p>"""
    events: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_events.MatterEvents"
    ]
    """<p>Describe the Matter events with the Matter event identifier mapped to the event fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCluster) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "attributes" in value:
        out["attributes"] = value["attributes"]
    if "commands" in value:
        import aws_sdk_iot_managed_integrations.types.matter_commands

        out["commands"] = (
            aws_sdk_iot_managed_integrations.types.matter_commands.serialize_json(
                value["commands"]
            )
        )
    if "events" in value:
        import aws_sdk_iot_managed_integrations.types.matter_events

        out["events"] = (
            aws_sdk_iot_managed_integrations.types.matter_events.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatterCluster:
    out: MatterCluster = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "attributes" in data:
        out["attributes"] = data["attributes"]
    if "commands" in data:
        import aws_sdk_iot_managed_integrations.types.matter_commands

        out["commands"] = (
            aws_sdk_iot_managed_integrations.types.matter_commands.deserialize_json(
                data["commands"]
            )
        )
    if "events" in data:
        import aws_sdk_iot_managed_integrations.types.matter_events

        out["events"] = (
            aws_sdk_iot_managed_integrations.types.matter_events.deserialize_json(
                data["events"]
            )
        )
    return out
