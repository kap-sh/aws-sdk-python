"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.compute_platform
    import aws_sdk_codedeploy.types.deployment_config_name
    import aws_sdk_codedeploy.types.minimum_healthy_hosts
    import aws_sdk_codedeploy.types.traffic_routing_config
    import aws_sdk_codedeploy.types.zonal_config


class CreateDeploymentConfigInput(TypedDict, closed=True):
    deployment_config_name: (
        "aws_sdk_codedeploy.types.deployment_config_name.DeploymentConfigName"
    )
    """<p>The name of the deployment configuration to create.</p>"""
    minimum_healthy_hosts: NotRequired[
        "aws_sdk_codedeploy.types.minimum_healthy_hosts.MinimumHealthyHosts"
    ]
    """<p>The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.</p> <p>The type parameter takes either of the following values:</p> <ul> <li> <p>HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.</p> </li> <li> <p>FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, CodeDeploy converts the percentage to the equivalent number of instances and rounds up fractional instances.</p> </li> </ul> <p>The value parameter takes an integer.</p> <p>For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95.</p>"""
    traffic_routing_config: NotRequired[
        "aws_sdk_codedeploy.types.traffic_routing_config.TrafficRoutingConfig"
    ]
    """<p>The configuration that specifies how the deployment traffic is routed.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>"""
    zonal_config: NotRequired["aws_sdk_codedeploy.types.zonal_config.ZonalConfig"]
    r"""<p>Configure the <code>ZonalConfig</code> object if you want CodeDeploy to deploy your application to one <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones\">Availability Zone</a> at a time, within an Amazon Web Services Region.</p> <p>For more information about the zonal configuration feature, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config\">zonal configuration</a> in the <i>CodeDeploy User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentConfigInput) -> dict:
    out: dict = {}
    out["deploymentConfigName"] = value["deployment_config_name"]
    if "minimum_healthy_hosts" in value:
        import aws_sdk_codedeploy.types.minimum_healthy_hosts

        out["minimumHealthyHosts"] = (
            aws_sdk_codedeploy.types.minimum_healthy_hosts.serialize_aws_json_1_1(
                value["minimum_healthy_hosts"]
            )
        )
    if "traffic_routing_config" in value:
        import aws_sdk_codedeploy.types.traffic_routing_config

        out["trafficRoutingConfig"] = (
            aws_sdk_codedeploy.types.traffic_routing_config.serialize_aws_json_1_1(
                value["traffic_routing_config"]
            )
        )
    if "compute_platform" in value:
        import aws_sdk_codedeploy.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentConfigInput:
    out: CreateDeploymentConfigInput = {}  # type: ignore[typeddict-item]
    if "deploymentConfigName" in data:
        out["deployment_config_name"] = data["deploymentConfigName"]
    else:
        raise DeserializationError(
            "CreateDeploymentConfigInput.deployment_config_name required"
        )
    if "minimumHealthyHosts" in data:
        import aws_sdk_codedeploy.types.minimum_healthy_hosts

        out["minimum_healthy_hosts"] = (
            aws_sdk_codedeploy.types.minimum_healthy_hosts.deserialize_aws_json_1_1(
                data["minimumHealthyHosts"]
            )
        )
    if "trafficRoutingConfig" in data:
        import aws_sdk_codedeploy.types.traffic_routing_config

        out["traffic_routing_config"] = (
            aws_sdk_codedeploy.types.traffic_routing_config.deserialize_aws_json_1_1(
                data["trafficRoutingConfig"]
            )
        )
    if "computePlatform" in data:
        import aws_sdk_codedeploy.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
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
