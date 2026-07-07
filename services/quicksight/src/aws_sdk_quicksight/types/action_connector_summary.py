"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.action_connector_error
    import aws_sdk_quicksight.types.action_connector_name
    import aws_sdk_quicksight.types.action_connector_type
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class ActionConnectorSummary(TypedDict, closed=True):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the action connector.</p>"""
    action_connector_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the action connector.</p>"""
    type: "aws_sdk_quicksight.types.action_connector_type.ActionConnectorType"
    """<p>The type of action connector (e.g., SALESFORCE, JIRA, CUSTOM, BEDROCK).</p>"""
    name: "aws_sdk_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>The name of the action connector.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the action connector was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The date and time when the action connector was last updated.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>The current status of the action connector.</p>"""
    error: NotRequired[
        "aws_sdk_quicksight.types.action_connector_error.ActionConnectorError"
    ]
    """<p>Error information if the action connector is in an error state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ActionConnectorId"] = value["action_connector_id"]
    import aws_sdk_quicksight.types.action_connector_type

    out["Type"] = aws_sdk_quicksight.types.action_connector_type.serialize_json(
        value["type"]
    )
    out["Name"] = value["name"]
    if "created_time" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    import aws_sdk_quicksight.types._prelude.timestamp

    out["LastUpdatedTime"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
        value["last_updated_time"]
    )
    if "status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["Status"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import aws_sdk_quicksight.types.action_connector_error

        out["Error"] = aws_sdk_quicksight.types.action_connector_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ActionConnectorSummary:
    out: ActionConnectorSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ActionConnectorSummary.arn required")
    if "ActionConnectorId" in data:
        out["action_connector_id"] = data["ActionConnectorId"]
    else:
        raise DeserializationError(
            "ActionConnectorSummary.action_connector_id required"
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.action_connector_type

        out["type"] = aws_sdk_quicksight.types.action_connector_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ActionConnectorSummary.type required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ActionConnectorSummary.name required")
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["last_updated_time"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("ActionConnectorSummary.last_updated_time required")
    if "Status" in data:
        import aws_sdk_quicksight.types.resource_status

        out["status"] = aws_sdk_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "Error" in data:
        import aws_sdk_quicksight.types.action_connector_error

        out["error"] = aws_sdk_quicksight.types.action_connector_error.deserialize_json(
            data["Error"]
        )
    return out
