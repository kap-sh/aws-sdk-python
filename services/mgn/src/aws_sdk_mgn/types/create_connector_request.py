"""Generated from Smithy shape ``com.amazonaws.mgn#CreateConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.connector_name
    import aws_sdk_mgn.types.connector_ssm_command_config
    import aws_sdk_mgn.types.ssm_instance_id
    import aws_sdk_mgn.types.tags_map


class CreateConnectorRequest(TypedDict):
    name: "aws_sdk_mgn.types.connector_name.ConnectorName"
    """<p>Create Connector request name.</p>"""
    ssm_instance_id: "aws_sdk_mgn.types.ssm_instance_id.SsmInstanceID"
    """<p>Create Connector request SSM instance ID.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Create Connector request tags.</p>"""
    ssm_command_config: NotRequired[
        "aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
    ]
    """<p>Create Connector request SSM command config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["ssmInstanceID"] = value["ssm_instance_id"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "ssm_command_config" in value:
        import aws_sdk_mgn.types.connector_ssm_command_config

        out["ssmCommandConfig"] = (
            aws_sdk_mgn.types.connector_ssm_command_config.serialize_json(
                value["ssm_command_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateConnectorRequest.name required")
    if "ssmInstanceID" in data:
        out["ssm_instance_id"] = data["ssmInstanceID"]
    else:
        raise DeserializationError("CreateConnectorRequest.ssm_instance_id required")
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "ssmCommandConfig" in data:
        import aws_sdk_mgn.types.connector_ssm_command_config

        out["ssm_command_config"] = (
            aws_sdk_mgn.types.connector_ssm_command_config.deserialize_json(
                data["ssmCommandConfig"]
            )
        )
    return out
