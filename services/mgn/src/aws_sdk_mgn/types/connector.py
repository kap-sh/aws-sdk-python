"""Generated from Smithy shape ``com.amazonaws.mgn#Connector``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.connector_id
    import aws_sdk_mgn.types.connector_name
    import aws_sdk_mgn.types.connector_ssm_command_config
    import aws_sdk_mgn.types.ssm_instance_id
    import aws_sdk_mgn.types.tags_map

class Connector(TypedDict):
    connector_id: NotRequired["aws_sdk_mgn.types.connector_id.ConnectorID"]
    """<p>Connector ID.</p>"""
    name: NotRequired["aws_sdk_mgn.types.connector_name.ConnectorName"]
    """<p>Connector name.</p>"""
    ssm_instance_id: NotRequired["aws_sdk_mgn.types.ssm_instance_id.SsmInstanceID"]
    """<p>Connector SSM instance ID.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Connector arn.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Connector tags.</p>"""
    ssm_command_config: NotRequired["aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"]
    """<p>Connector SSM command config.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    if "connector_id" in value:
        out["connectorID"] = value["connector_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "ssm_instance_id" in value:
        out["ssmInstanceID"] = value["ssm_instance_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map
        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "ssm_command_config" in value:
        import aws_sdk_mgn.types.connector_ssm_command_config
        out["ssmCommandConfig"] = aws_sdk_mgn.types.connector_ssm_command_config.serialize_json(value["ssm_command_config"])
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if "connectorID" in data:
        out["connector_id"] = data["connectorID"]
    if "name" in data:
        out["name"] = data["name"]
    if "ssmInstanceID" in data:
        out["ssm_instance_id"] = data["ssmInstanceID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map
        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "ssmCommandConfig" in data:
        import aws_sdk_mgn.types.connector_ssm_command_config
        out["ssm_command_config"] = aws_sdk_mgn.types.connector_ssm_command_config.deserialize_json(data["ssmCommandConfig"])
    return out