"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerGroupPortMappingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.compute_name
    import aws_sdk_gamelift.types.container_group_definition_arn
    import aws_sdk_gamelift.types.container_group_port_mapping_list
    import aws_sdk_gamelift.types.container_group_type
    import aws_sdk_gamelift.types.fleet_id
    import aws_sdk_gamelift.types.instance_id
    import aws_sdk_gamelift.types.location_string_model


class DescribeContainerGroupPortMappingsOutput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the container fleet.</p>"""
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The location of the fleet instance, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""
    container_group_definition_arn: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_arn.ContainerGroupDefinitionArn"
    ]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to the container group definition. The ARN value also identifies the specific container group definition version in use.</p>"""
    container_group_type: NotRequired[
        "aws_sdk_gamelift.types.container_group_type.ContainerGroupType"
    ]
    """<p>The type of container group that was specified in the request. Valid values are <code>GAME_SERVER</code> or <code>PER_INSTANCE</code>.</p>"""
    compute_name: NotRequired["aws_sdk_gamelift.types.compute_name.ComputeName"]
    """<p>A unique identifier for the compute resource running the game server container group. Returned when <code>ContainerGroupType</code> is <code>GAME_SERVER</code>.</p>"""
    instance_id: NotRequired["aws_sdk_gamelift.types.instance_id.InstanceId"]
    """<p>A unique identifier for the fleet instance. For <code>GAME_SERVER</code> requests, this is the instance running the specified compute. For <code>PER_INSTANCE</code> requests, this is the instance specified in the request.</p>"""
    container_group_port_mappings: NotRequired[
        "aws_sdk_gamelift.types.container_group_port_mapping_list.ContainerGroupPortMappingList"
    ]
    """<p>A list of <code>ContainerGroupPortMapping</code> objects that describe the port mappings for each container in the container group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerGroupPortMappingsOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "location" in value:
        out["Location"] = value["location"]
    if "container_group_definition_arn" in value:
        out["ContainerGroupDefinitionArn"] = value["container_group_definition_arn"]
    if "container_group_type" in value:
        import aws_sdk_gamelift.types.container_group_type

        out["ContainerGroupType"] = (
            aws_sdk_gamelift.types.container_group_type.serialize_aws_json_1_1(
                value["container_group_type"]
            )
        )
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "container_group_port_mappings" in value:
        import aws_sdk_gamelift.types.container_group_port_mapping_list

        out["ContainerGroupPortMappings"] = (
            aws_sdk_gamelift.types.container_group_port_mapping_list.serialize_aws_json_1_1(
                value["container_group_port_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerGroupPortMappingsOutput:
    out: DescribeContainerGroupPortMappingsOutput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "ContainerGroupDefinitionArn" in data:
        out["container_group_definition_arn"] = data["ContainerGroupDefinitionArn"]
    if "ContainerGroupType" in data:
        import aws_sdk_gamelift.types.container_group_type

        out["container_group_type"] = (
            aws_sdk_gamelift.types.container_group_type.deserialize_aws_json_1_1(
                data["ContainerGroupType"]
            )
        )
    if "ComputeName" in data:
        out["compute_name"] = data["ComputeName"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ContainerGroupPortMappings" in data:
        import aws_sdk_gamelift.types.container_group_port_mapping_list

        out["container_group_port_mappings"] = (
            aws_sdk_gamelift.types.container_group_port_mapping_list.deserialize_aws_json_1_1(
                data["ContainerGroupPortMappings"]
            )
        )
    return out
