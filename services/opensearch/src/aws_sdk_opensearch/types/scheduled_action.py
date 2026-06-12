"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.action_severity
    import aws_sdk_opensearch.types.action_status
    import aws_sdk_opensearch.types.action_type
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.long
    import aws_sdk_opensearch.types.scheduled_by
    import aws_sdk_opensearch.types.string


class ScheduledAction(TypedDict):
    id: "aws_sdk_opensearch.types.string.String"
    """<p>The unique identifier of the scheduled action.</p>"""
    type: "aws_sdk_opensearch.types.action_type.ActionType"
    """<p>The type of action that will be taken on the domain.</p>"""
    severity: "aws_sdk_opensearch.types.action_severity.ActionSeverity"
    """<p>The severity of the action.</p>"""
    scheduled_time: "aws_sdk_opensearch.types.long.Long"
    """<p>The time when the change is scheduled to happen.</p>"""
    description: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A description of the action to be taken.</p>"""
    scheduled_by: NotRequired["aws_sdk_opensearch.types.scheduled_by.ScheduledBy"]
    """<p>Whether the action was scheduled manually (<code>CUSTOMER</code>, or by OpenSearch Service automatically (<code>SYSTEM</code>).</p>"""
    status: NotRequired["aws_sdk_opensearch.types.action_status.ActionStatus"]
    """<p>The current status of the scheduled action.</p>"""
    mandatory: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether the action is required or optional.</p>"""
    cancellable: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether or not the scheduled action is cancellable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAction) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_opensearch.types.action_type

    out["Type"] = aws_sdk_opensearch.types.action_type.serialize_json(value["type"])
    import aws_sdk_opensearch.types.action_severity

    out["Severity"] = aws_sdk_opensearch.types.action_severity.serialize_json(
        value["severity"]
    )
    out["ScheduledTime"] = value["scheduled_time"]
    if "description" in value:
        out["Description"] = value["description"]
    if "scheduled_by" in value:
        import aws_sdk_opensearch.types.scheduled_by

        out["ScheduledBy"] = aws_sdk_opensearch.types.scheduled_by.serialize_json(
            value["scheduled_by"]
        )
    if "status" in value:
        import aws_sdk_opensearch.types.action_status

        out["Status"] = aws_sdk_opensearch.types.action_status.serialize_json(
            value["status"]
        )
    if "mandatory" in value:
        out["Mandatory"] = value["mandatory"]
    if "cancellable" in value:
        out["Cancellable"] = value["cancellable"]
    return out


def deserialize_json(data: dict) -> ScheduledAction:
    out: ScheduledAction = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ScheduledAction.id required")
    if "Type" in data:
        import aws_sdk_opensearch.types.action_type

        out["type"] = aws_sdk_opensearch.types.action_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ScheduledAction.type required")
    if "Severity" in data:
        import aws_sdk_opensearch.types.action_severity

        out["severity"] = aws_sdk_opensearch.types.action_severity.deserialize_json(
            data["Severity"]
        )
    else:
        raise DeserializationError("ScheduledAction.severity required")
    if "ScheduledTime" in data:
        out["scheduled_time"] = data["ScheduledTime"]
    else:
        raise DeserializationError("ScheduledAction.scheduled_time required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ScheduledBy" in data:
        import aws_sdk_opensearch.types.scheduled_by

        out["scheduled_by"] = aws_sdk_opensearch.types.scheduled_by.deserialize_json(
            data["ScheduledBy"]
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.action_status

        out["status"] = aws_sdk_opensearch.types.action_status.deserialize_json(
            data["Status"]
        )
    if "Mandatory" in data:
        out["mandatory"] = data["Mandatory"]
    if "Cancellable" in data:
        out["cancellable"] = data["Cancellable"]
    return out
