"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.action_connector_description
    import aws_sdk_quicksight.types.action_connector_error
    import aws_sdk_quicksight.types.action_connector_name
    import aws_sdk_quicksight.types.action_connector_type
    import aws_sdk_quicksight.types.action_id_list
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.read_auth_config
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class ActionConnector(TypedDict, closed=True):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the action connector.</p>"""
    action_connector_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the action connector.</p>"""
    type: "aws_sdk_quicksight.types.action_connector_type.ActionConnectorType"
    """<p>The type of action connector.</p>"""
    name: "aws_sdk_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>The name of the action connector.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the action connector was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The date and time when the action connector was last updated.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>The current status of the action connector.</p>"""
    error: NotRequired[
        "aws_sdk_quicksight.types.action_connector_error.ActionConnectorError"
    ]
    """<p>Error information if the action connector is in an error state.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.action_connector_description.ActionConnectorDescription"
    ]
    """<p>The description of the action connector.</p>"""
    authentication_config: NotRequired[
        "aws_sdk_quicksight.types.read_auth_config.ReadAuthConfig"
    ]
    """<p>The authentication configuration used to connect to the external service.</p>"""
    enabled_actions: NotRequired["aws_sdk_quicksight.types.action_id_list.ActionIdList"]
    """<p>The list of actions that are enabled for this connector.</p>"""
    vpc_connection_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the VPC connection used for secure connectivity to the external service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnector) -> dict:
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
    if "description" in value:
        out["Description"] = value["description"]
    if "authentication_config" in value:
        import aws_sdk_quicksight.types.read_auth_config

        out["AuthenticationConfig"] = (
            aws_sdk_quicksight.types.read_auth_config.serialize_json(
                value["authentication_config"]
            )
        )
    if "enabled_actions" in value:
        import aws_sdk_quicksight.types.action_id_list

        out["EnabledActions"] = aws_sdk_quicksight.types.action_id_list.serialize_json(
            value["enabled_actions"]
        )
    if "vpc_connection_arn" in value:
        out["VpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> ActionConnector:
    out: ActionConnector = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ActionConnector.arn required")
    if "ActionConnectorId" in data:
        out["action_connector_id"] = data["ActionConnectorId"]
    else:
        raise DeserializationError("ActionConnector.action_connector_id required")
    if "Type" in data:
        import aws_sdk_quicksight.types.action_connector_type

        out["type"] = aws_sdk_quicksight.types.action_connector_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ActionConnector.type required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ActionConnector.name required")
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
        raise DeserializationError("ActionConnector.last_updated_time required")
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
    if "Description" in data:
        out["description"] = data["Description"]
    if "AuthenticationConfig" in data:
        import aws_sdk_quicksight.types.read_auth_config

        out["authentication_config"] = (
            aws_sdk_quicksight.types.read_auth_config.deserialize_json(
                data["AuthenticationConfig"]
            )
        )
    if "EnabledActions" in data:
        import aws_sdk_quicksight.types.action_id_list

        out["enabled_actions"] = (
            aws_sdk_quicksight.types.action_id_list.deserialize_json(
                data["EnabledActions"]
            )
        )
    if "VpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    return out
