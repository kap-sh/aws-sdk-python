"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.change_action
    import aws_sdk_networkmanager.types.change_status
    import aws_sdk_networkmanager.types.change_type
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_change_event_values
    import aws_sdk_networkmanager.types.date_time


class CoreNetworkChangeEvent(TypedDict):
    type: NotRequired["aws_sdk_networkmanager.types.change_type.ChangeType"]
    """<p>Describes the type of change event. </p>"""
    action: NotRequired["aws_sdk_networkmanager.types.change_action.ChangeAction"]
    """<p>The action taken for the change event.</p>"""
    identifier_path: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>Uniquely identifies the path for a change within the changeset. For example, the <code>IdentifierPath</code> for a core network segment change might be <code>\"CORE_NETWORK_SEGMENT/us-east-1/devsegment\"</code>.</p>"""
    event_time: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp for an event change in status.</p>"""
    status: NotRequired["aws_sdk_networkmanager.types.change_status.ChangeStatus"]
    """<p>The status of the core network change event.</p>"""
    values: NotRequired[
        "aws_sdk_networkmanager.types.core_network_change_event_values.CoreNetworkChangeEventValues"
    ]
    """<p>Details of the change event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeEvent) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_networkmanager.types.change_type

        out["Type"] = aws_sdk_networkmanager.types.change_type.serialize_json(
            value["type"]
        )
    if "action" in value:
        import aws_sdk_networkmanager.types.change_action

        out["Action"] = aws_sdk_networkmanager.types.change_action.serialize_json(
            value["action"]
        )
    if "identifier_path" in value:
        out["IdentifierPath"] = value["identifier_path"]
    if "event_time" in value:
        import aws_sdk_networkmanager.types.date_time

        out["EventTime"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["event_time"]
        )
    if "status" in value:
        import aws_sdk_networkmanager.types.change_status

        out["Status"] = aws_sdk_networkmanager.types.change_status.serialize_json(
            value["status"]
        )
    if "values" in value:
        import aws_sdk_networkmanager.types.core_network_change_event_values

        out["Values"] = (
            aws_sdk_networkmanager.types.core_network_change_event_values.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkChangeEvent:
    out: CoreNetworkChangeEvent = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_networkmanager.types.change_type

        out["type"] = aws_sdk_networkmanager.types.change_type.deserialize_json(
            data["Type"]
        )
    if "Action" in data:
        import aws_sdk_networkmanager.types.change_action

        out["action"] = aws_sdk_networkmanager.types.change_action.deserialize_json(
            data["Action"]
        )
    if "IdentifierPath" in data:
        out["identifier_path"] = data["IdentifierPath"]
    if "EventTime" in data:
        import aws_sdk_networkmanager.types.date_time

        out["event_time"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["EventTime"]
        )
    if "Status" in data:
        import aws_sdk_networkmanager.types.change_status

        out["status"] = aws_sdk_networkmanager.types.change_status.deserialize_json(
            data["Status"]
        )
    if "Values" in data:
        import aws_sdk_networkmanager.types.core_network_change_event_values

        out["values"] = (
            aws_sdk_networkmanager.types.core_network_change_event_values.deserialize_json(
                data["Values"]
            )
        )
    return out
