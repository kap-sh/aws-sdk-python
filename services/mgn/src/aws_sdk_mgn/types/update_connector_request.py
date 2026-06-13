"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.connector_id
    import aws_sdk_mgn.types.connector_name
    import aws_sdk_mgn.types.connector_ssm_command_config


class UpdateConnectorRequest(TypedDict):
    connector_id: "aws_sdk_mgn.types.connector_id.ConnectorID"
    """<p>Update Connector request connector ID.</p>"""
    name: NotRequired["aws_sdk_mgn.types.connector_name.ConnectorName"]
    """<p>Update Connector request name.</p>"""
    ssm_command_config: NotRequired[
        "aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
    ]
    """<p>Update Connector request SSM command config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRequest) -> dict:
    out: dict = {}
    out["connectorID"] = value["connector_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "ssm_command_config" in value:
        import aws_sdk_mgn.types.connector_ssm_command_config

        out["ssmCommandConfig"] = (
            aws_sdk_mgn.types.connector_ssm_command_config.serialize_json(
                value["ssm_command_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorRequest:
    out: UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
    if "connectorID" in data:
        out["connector_id"] = data["connectorID"]
    else:
        raise DeserializationError("UpdateConnectorRequest.connector_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "ssmCommandConfig" in data:
        import aws_sdk_mgn.types.connector_ssm_command_config

        out["ssm_command_config"] = (
            aws_sdk_mgn.types.connector_ssm_command_config.deserialize_json(
                data["ssmCommandConfig"]
            )
        )
    return out
