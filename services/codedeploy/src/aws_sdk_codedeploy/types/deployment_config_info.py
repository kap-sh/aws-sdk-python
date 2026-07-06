"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentConfigInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.compute_platform
    import aws_sdk_codedeploy.types.deployment_config_id
    import aws_sdk_codedeploy.types.deployment_config_name
    import aws_sdk_codedeploy.types.minimum_healthy_hosts
    import aws_sdk_codedeploy.types.timestamp
    import aws_sdk_codedeploy.types.traffic_routing_config
    import aws_sdk_codedeploy.types.zonal_config


class DeploymentConfigInfo(TypedDict, closed=True):
    deployment_config_id: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_id.DeploymentConfigId"
    ]
    """<p>The deployment configuration ID.</p>"""
    deployment_config_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p>The deployment configuration name.</p>"""
    minimum_healthy_hosts: NotRequired[
        "aws_sdk_codedeploy.types.minimum_healthy_hosts.MinimumHealthyHosts"
    ]
    """<p>Information about the number or percentage of minimum healthy instances.</p>"""
    create_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>The time at which the deployment configuration was created.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>"""
    traffic_routing_config: NotRequired[
        "aws_sdk_codedeploy.types.traffic_routing_config.TrafficRoutingConfig"
    ]
    """<p>The configuration that specifies how the deployment traffic is routed. Used for deployments with a Lambda or Amazon ECS compute platform only.</p>"""
    zonal_config: NotRequired["aws_sdk_codedeploy.types.zonal_config.ZonalConfig"]
    """<p>Information about a zonal configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfigInfo) -> dict:
    out: dict = {}
    if "deployment_config_id" in value:
        out["deploymentConfigId"] = value["deployment_config_id"]
    if "deployment_config_name" in value:
        out["deploymentConfigName"] = value["deployment_config_name"]
    if "minimum_healthy_hosts" in value:
        import aws_sdk_codedeploy.types.minimum_healthy_hosts

        out["minimumHealthyHosts"] = (
            aws_sdk_codedeploy.types.minimum_healthy_hosts.serialize_aws_json_1_1(
                value["minimum_healthy_hosts"]
            )
        )
    if "create_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["createTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "compute_platform" in value:
        import aws_sdk_codedeploy.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    if "traffic_routing_config" in value:
        import aws_sdk_codedeploy.types.traffic_routing_config

        out["trafficRoutingConfig"] = (
            aws_sdk_codedeploy.types.traffic_routing_config.serialize_aws_json_1_1(
                value["traffic_routing_config"]
            )
        )
    if "zonal_config" in value:
        import aws_sdk_codedeploy.types.zonal_config

        out["zonalConfig"] = (
            aws_sdk_codedeploy.types.zonal_config.serialize_aws_json_1_1(
                value["zonal_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentConfigInfo:
    out: DeploymentConfigInfo = {}  # type: ignore[typeddict-item]
    if "deploymentConfigId" in data:
        out["deployment_config_id"] = data["deploymentConfigId"]
    if "deploymentConfigName" in data:
        out["deployment_config_name"] = data["deploymentConfigName"]
    if "minimumHealthyHosts" in data:
        import aws_sdk_codedeploy.types.minimum_healthy_hosts

        out["minimum_healthy_hosts"] = (
            aws_sdk_codedeploy.types.minimum_healthy_hosts.deserialize_aws_json_1_1(
                data["minimumHealthyHosts"]
            )
        )
    if "createTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["create_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["createTime"]
            )
        )
    if "computePlatform" in data:
        import aws_sdk_codedeploy.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    if "trafficRoutingConfig" in data:
        import aws_sdk_codedeploy.types.traffic_routing_config

        out["traffic_routing_config"] = (
            aws_sdk_codedeploy.types.traffic_routing_config.deserialize_aws_json_1_1(
                data["trafficRoutingConfig"]
            )
        )
    if "zonalConfig" in data:
        import aws_sdk_codedeploy.types.zonal_config

        out["zonal_config"] = (
            aws_sdk_codedeploy.types.zonal_config.deserialize_aws_json_1_1(
                data["zonalConfig"]
            )
        )
    return out
