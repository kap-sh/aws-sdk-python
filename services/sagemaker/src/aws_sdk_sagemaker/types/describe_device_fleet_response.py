"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDeviceFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_fleet_arn
    import aws_sdk_sagemaker.types.device_fleet_description
    import aws_sdk_sagemaker.types.edge_output_config
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.iot_role_alias
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeDeviceFleetResponse(TypedDict, closed=True):
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet.</p>"""
    device_fleet_arn: NotRequired[
        "aws_sdk_sagemaker.types.device_fleet_arn.DeviceFleetArn"
    ]
    """<p>The The Amazon Resource Name (ARN) of the fleet.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.edge_output_config.EdgeOutputConfig"
    ]
    """<p>The output configuration for storing sampled data.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.device_fleet_description.DeviceFleetDescription"
    ]
    """<p>A description of the fleet.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Timestamp of when the device fleet was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Timestamp of when the device fleet was last updated.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that has access to Amazon Web Services Internet of Things (IoT).</p>"""
    iot_role_alias: NotRequired["aws_sdk_sagemaker.types.iot_role_alias.IotRoleAlias"]
    """<p>The Amazon Resource Name (ARN) alias created in Amazon Web Services Internet of Things (IoT).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeviceFleetResponse) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "device_fleet_arn" in value:
        out["DeviceFleetArn"] = value["device_fleet_arn"]
    if "output_config" in value:
        import aws_sdk_sagemaker.types.edge_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.edge_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "iot_role_alias" in value:
        out["IotRoleAlias"] = value["iot_role_alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeviceFleetResponse:
    out: DescribeDeviceFleetResponse = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "DeviceFleetArn" in data:
        out["device_fleet_arn"] = data["DeviceFleetArn"]
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.edge_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.edge_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "IotRoleAlias" in data:
        out["iot_role_alias"] = data["IotRoleAlias"]
    return out
