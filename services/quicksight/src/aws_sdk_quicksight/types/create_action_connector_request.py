"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateActionConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_description
    import aws_sdk_quicksight.types.action_connector_name
    import aws_sdk_quicksight.types.action_connector_type
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.auth_config
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.tag_list


class CreateActionConnectorRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID associated with the action connector.</p>"""
    action_connector_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>A unique identifier for the action connector. This ID must be unique within the Amazon Web Services account. The <code>ActionConnectorId</code> must not start with the prefix <code>quicksuite-</code> </p>"""
    name: "aws_sdk_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>A descriptive name for the action connector.</p>"""
    type: "aws_sdk_quicksight.types.action_connector_type.ActionConnectorType"
    """<p>The type of action connector.</p>"""
    authentication_config: "aws_sdk_quicksight.types.auth_config.AuthConfig"
    """<p>The authentication configuration for connecting to the external service. This includes the authentication type, base URL, and authentication metadata such as client credentials or API keys.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.action_connector_description.ActionConnectorDescription"
    ]
    """<p>An optional description of the action connector.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions configuration that defines which users, groups, or namespaces can access this action connector and what operations they can perform.</p>"""
    vpc_connection_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the VPC connection to use for secure connectivity to the external service.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>A list of tags to apply to the action connector for resource management and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActionConnectorRequest) -> dict:
    out: dict = {}
    out["ActionConnectorId"] = value["action_connector_id"]
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.action_connector_type

    out["Type"] = aws_sdk_quicksight.types.action_connector_type.serialize_json(
        value["type"]
    )
    import aws_sdk_quicksight.types.auth_config

    out["AuthenticationConfig"] = aws_sdk_quicksight.types.auth_config.serialize_json(
        value["authentication_config"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "vpc_connection_arn" in value:
        out["VpcConnectionArn"] = value["vpc_connection_arn"]
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateActionConnectorRequest:
    out: CreateActionConnectorRequest = {}  # type: ignore[typeddict-item]
    if "ActionConnectorId" in data:
        out["action_connector_id"] = data["ActionConnectorId"]
    else:
        raise DeserializationError(
            "CreateActionConnectorRequest.action_connector_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateActionConnectorRequest.name required")
    if "Type" in data:
        import aws_sdk_quicksight.types.action_connector_type

        out["type"] = aws_sdk_quicksight.types.action_connector_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateActionConnectorRequest.type required")
    if "AuthenticationConfig" in data:
        import aws_sdk_quicksight.types.auth_config

        out["authentication_config"] = (
            aws_sdk_quicksight.types.auth_config.deserialize_json(
                data["AuthenticationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateActionConnectorRequest.authentication_config required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "VpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
