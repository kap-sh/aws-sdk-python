"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateActionConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_description
    import aws_sdk_quicksight.types.action_connector_name
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.auth_config
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class UpdateActionConnectorRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that contains the action connector to update.</p>"""
    action_connector_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the action connector to update.</p>"""
    name: "aws_sdk_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>The new name for the action connector.</p>"""
    authentication_config: "aws_sdk_quicksight.types.auth_config.AuthConfig"
    """<p>The updated authentication configuration for connecting to the external service.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.action_connector_description.ActionConnectorDescription"
    ]
    """<p>The updated description of the action connector.</p>"""
    vpc_connection_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The updated ARN of the VPC connection to use for secure connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.auth_config

    out["AuthenticationConfig"] = aws_sdk_quicksight.types.auth_config.serialize_json(
        value["authentication_config"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_connection_arn" in value:
        out["VpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> UpdateActionConnectorRequest:
    out: UpdateActionConnectorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateActionConnectorRequest.name required")
    if "AuthenticationConfig" in data:
        import aws_sdk_quicksight.types.auth_config

        out["authentication_config"] = (
            aws_sdk_quicksight.types.auth_config.deserialize_json(
                data["AuthenticationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateActionConnectorRequest.authentication_config required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "VpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    return out
