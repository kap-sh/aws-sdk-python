"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateDeviceFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_fleet_description
    import capo_sagemaker.types.edge_output_config
    import capo_sagemaker.types.enable_iot_role_alias
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateDeviceFleetRequest(TypedDict, closed=True):
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet that the device belongs to.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that has access to Amazon Web Services Internet of Things (IoT).</p>"""
    description: NotRequired[
        "capo_sagemaker.types.device_fleet_description.DeviceFleetDescription"
    ]
    """<p>A description of the fleet.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.edge_output_config.EdgeOutputConfig"
    ]
    """<p>The output configuration for storing sample data collected by the fleet.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Creates tags for the specified fleet.</p>"""
    enable_iot_role_alias: NotRequired[
        "capo_sagemaker.types.enable_iot_role_alias.EnableIotRoleAlias"
    ]
    r"""<p>Whether to create an Amazon Web Services IoT Role Alias during device fleet creation. The name of the role alias generated will match this pattern: \"SageMakerEdge-{DeviceFleetName}\".</p> <p>For example, if your device fleet is called \"demo-fleet\", the name of the role alias will be \"SageMakerEdge-demo-fleet\".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeviceFleetRequest) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "output_config" in value:
        import capo_sagemaker.types.edge_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.edge_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "enable_iot_role_alias" in value:
        out["EnableIotRoleAlias"] = value["enable_iot_role_alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeviceFleetRequest:
    out: CreateDeviceFleetRequest = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "OutputConfig" in data:
        import capo_sagemaker.types.edge_output_config

        out["output_config"] = (
            capo_sagemaker.types.edge_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "EnableIotRoleAlias" in data:
        out["enable_iot_role_alias"] = data["EnableIotRoleAlias"]
    return out
