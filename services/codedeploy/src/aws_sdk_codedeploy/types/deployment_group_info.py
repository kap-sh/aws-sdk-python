"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentGroupInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.alarm_configuration
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.auto_rollback_configuration
    import aws_sdk_codedeploy.types.auto_scaling_group_list
    import aws_sdk_codedeploy.types.blue_green_deployment_configuration
    import aws_sdk_codedeploy.types.boolean
    import aws_sdk_codedeploy.types.compute_platform
    import aws_sdk_codedeploy.types.deployment_config_name
    import aws_sdk_codedeploy.types.deployment_group_id
    import aws_sdk_codedeploy.types.deployment_group_name
    import aws_sdk_codedeploy.types.deployment_style
    import aws_sdk_codedeploy.types.ec2_tag_filter_list
    import aws_sdk_codedeploy.types.ec2_tag_set
    import aws_sdk_codedeploy.types.ecs_service_list
    import aws_sdk_codedeploy.types.last_deployment_info
    import aws_sdk_codedeploy.types.load_balancer_info
    import aws_sdk_codedeploy.types.on_premises_tag_set
    import aws_sdk_codedeploy.types.outdated_instances_strategy
    import aws_sdk_codedeploy.types.revision_location
    import aws_sdk_codedeploy.types.role
    import aws_sdk_codedeploy.types.tag_filter_list
    import aws_sdk_codedeploy.types.trigger_config_list


class DeploymentGroupInfo(TypedDict, closed=True):
    application_name: NotRequired[
        "aws_sdk_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The application name.</p>"""
    deployment_group_id: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_id.DeploymentGroupId"
    ]
    """<p>The deployment group ID.</p>"""
    deployment_group_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_name.DeploymentGroupName"
    ]
    """<p>The deployment group name.</p>"""
    deployment_config_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p>The deployment configuration name.</p>"""
    ec2_tag_filters: NotRequired[
        "aws_sdk_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
    ]
    """<p>The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags.</p>"""
    on_premises_instance_tag_filters: NotRequired[
        "aws_sdk_codedeploy.types.tag_filter_list.TagFilterList"
    ]
    """<p>The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags.</p>"""
    auto_scaling_groups: NotRequired[
        "aws_sdk_codedeploy.types.auto_scaling_group_list.AutoScalingGroupList"
    ]
    """<p>A list of associated Auto Scaling groups.</p>"""
    service_role_arn: NotRequired["aws_sdk_codedeploy.types.role.Role"]
    r"""<p>A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to Amazon Web Services services on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html\">Create a Service Role for CodeDeploy</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    target_revision: NotRequired[
        "aws_sdk_codedeploy.types.revision_location.RevisionLocation"
    ]
    """<p>Information about the deployment group's target revision, including type and location.</p>"""
    trigger_configurations: NotRequired[
        "aws_sdk_codedeploy.types.trigger_config_list.TriggerConfigList"
    ]
    """<p>Information about triggers associated with the deployment group.</p>"""
    alarm_configuration: NotRequired[
        "aws_sdk_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>A list of alarms associated with the deployment group.</p>"""
    auto_rollback_configuration: NotRequired[
        "aws_sdk_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Information about the automatic rollback configuration associated with the deployment group.</p>"""
    deployment_style: NotRequired[
        "aws_sdk_codedeploy.types.deployment_style.DeploymentStyle"
    ]
    """<p>Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.</p>"""
    outdated_instances_strategy: NotRequired[
        "aws_sdk_codedeploy.types.outdated_instances_strategy.OutdatedInstancesStrategy"
    ]
    """<p>Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.</p> <p>If this option is set to <code>UPDATE</code> or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.</p> <p>If this option is set to <code>IGNORE</code>, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.</p>"""
    blue_green_deployment_configuration: NotRequired[
        "aws_sdk_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
    ]
    """<p>Information about blue/green deployment options for a deployment group.</p>"""
    load_balancer_info: NotRequired[
        "aws_sdk_codedeploy.types.load_balancer_info.LoadBalancerInfo"
    ]
    """<p>Information about the load balancer to use in a deployment.</p>"""
    last_successful_deployment: NotRequired[
        "aws_sdk_codedeploy.types.last_deployment_info.LastDeploymentInfo"
    ]
    """<p>Information about the most recent successful deployment to the deployment group.</p>"""
    last_attempted_deployment: NotRequired[
        "aws_sdk_codedeploy.types.last_deployment_info.LastDeploymentInfo"
    ]
    """<p>Information about the most recent attempted deployment to the deployment group.</p>"""
    ec2_tag_set: NotRequired["aws_sdk_codedeploy.types.ec2_tag_set.EC2TagSet"]
    """<p>Information about groups of tags applied to an Amazon EC2 instance. The deployment group includes only Amazon EC2 instances identified by all of the tag groups. Cannot be used in the same call as ec2TagFilters.</p>"""
    on_premises_tag_set: NotRequired[
        "aws_sdk_codedeploy.types.on_premises_tag_set.OnPremisesTagSet"
    ]
    """<p>Information about groups of tags applied to an on-premises instance. The deployment group includes only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>"""
    ecs_services: NotRequired[
        "aws_sdk_codedeploy.types.ecs_service_list.ECSServiceList"
    ]
    """<p> The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <code><clustername>:<servicename></code>. </p>"""
    termination_hook_enabled: "aws_sdk_codedeploy.types.boolean.Boolean"
    r"""<p>Indicates whether the deployment group was configured to have CodeDeploy install a termination hook into an Auto Scaling group.</p> <p>For more information about the termination hook, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors\">How Amazon EC2 Auto Scaling works with CodeDeploy</a> in the <i>CodeDeploy User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentGroupInfo) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "deployment_group_id" in value:
        out["deploymentGroupId"] = value["deployment_group_id"]
    if "deployment_group_name" in value:
        out["deploymentGroupName"] = value["deployment_group_name"]
    if "deployment_config_name" in value:
        out["deploymentConfigName"] = value["deployment_config_name"]
    if "ec2_tag_filters" in value:
        import aws_sdk_codedeploy.types.ec2_tag_filter_list

        out["ec2TagFilters"] = (
            aws_sdk_codedeploy.types.ec2_tag_filter_list.serialize_aws_json_1_1(
                value["ec2_tag_filters"]
            )
        )
    if "on_premises_instance_tag_filters" in value:
        import aws_sdk_codedeploy.types.tag_filter_list

        out["onPremisesInstanceTagFilters"] = (
            aws_sdk_codedeploy.types.tag_filter_list.serialize_aws_json_1_1(
                value["on_premises_instance_tag_filters"]
            )
        )
    if "auto_scaling_groups" in value:
        import aws_sdk_codedeploy.types.auto_scaling_group_list

        out["autoScalingGroups"] = (
            aws_sdk_codedeploy.types.auto_scaling_group_list.serialize_aws_json_1_1(
                value["auto_scaling_groups"]
            )
        )
    if "service_role_arn" in value:
        out["serviceRoleArn"] = value["service_role_arn"]
    if "target_revision" in value:
        import aws_sdk_codedeploy.types.revision_location

        out["targetRevision"] = (
            aws_sdk_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["target_revision"]
            )
        )
    if "trigger_configurations" in value:
        import aws_sdk_codedeploy.types.trigger_config_list

        out["triggerConfigurations"] = (
            aws_sdk_codedeploy.types.trigger_config_list.serialize_aws_json_1_1(
                value["trigger_configurations"]
            )
        )
    if "alarm_configuration" in value:
        import aws_sdk_codedeploy.types.alarm_configuration

        out["alarmConfiguration"] = (
            aws_sdk_codedeploy.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "auto_rollback_configuration" in value:
        import aws_sdk_codedeploy.types.auto_rollback_configuration

        out["autoRollbackConfiguration"] = (
            aws_sdk_codedeploy.types.auto_rollback_configuration.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    if "deployment_style" in value:
        import aws_sdk_codedeploy.types.deployment_style

        out["deploymentStyle"] = (
            aws_sdk_codedeploy.types.deployment_style.serialize_aws_json_1_1(
                value["deployment_style"]
            )
        )
    if "outdated_instances_strategy" in value:
        import aws_sdk_codedeploy.types.outdated_instances_strategy

        out["outdatedInstancesStrategy"] = (
            aws_sdk_codedeploy.types.outdated_instances_strategy.serialize_aws_json_1_1(
                value["outdated_instances_strategy"]
            )
        )
    if "blue_green_deployment_configuration" in value:
        import aws_sdk_codedeploy.types.blue_green_deployment_configuration

        out["blueGreenDeploymentConfiguration"] = (
            aws_sdk_codedeploy.types.blue_green_deployment_configuration.serialize_aws_json_1_1(
                value["blue_green_deployment_configuration"]
            )
        )
    if "load_balancer_info" in value:
        import aws_sdk_codedeploy.types.load_balancer_info

        out["loadBalancerInfo"] = (
            aws_sdk_codedeploy.types.load_balancer_info.serialize_aws_json_1_1(
                value["load_balancer_info"]
            )
        )
    if "last_successful_deployment" in value:
        import aws_sdk_codedeploy.types.last_deployment_info

        out["lastSuccessfulDeployment"] = (
            aws_sdk_codedeploy.types.last_deployment_info.serialize_aws_json_1_1(
                value["last_successful_deployment"]
            )
        )
    if "last_attempted_deployment" in value:
        import aws_sdk_codedeploy.types.last_deployment_info

        out["lastAttemptedDeployment"] = (
            aws_sdk_codedeploy.types.last_deployment_info.serialize_aws_json_1_1(
                value["last_attempted_deployment"]
            )
        )
    if "ec2_tag_set" in value:
        import aws_sdk_codedeploy.types.ec2_tag_set

        out["ec2TagSet"] = aws_sdk_codedeploy.types.ec2_tag_set.serialize_aws_json_1_1(
            value["ec2_tag_set"]
        )
    if "on_premises_tag_set" in value:
        import aws_sdk_codedeploy.types.on_premises_tag_set

        out["onPremisesTagSet"] = (
            aws_sdk_codedeploy.types.on_premises_tag_set.serialize_aws_json_1_1(
                value["on_premises_tag_set"]
            )
        )
    if "compute_platform" in value:
        import aws_sdk_codedeploy.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    if "ecs_services" in value:
        import aws_sdk_codedeploy.types.ecs_service_list

        out["ecsServices"] = (
            aws_sdk_codedeploy.types.ecs_service_list.serialize_aws_json_1_1(
                value["ecs_services"]
            )
        )
    out["terminationHookEnabled"] = value.get("termination_hook_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentGroupInfo:
    out: DeploymentGroupInfo = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "deploymentGroupId" in data:
        out["deployment_group_id"] = data["deploymentGroupId"]
    if "deploymentGroupName" in data:
        out["deployment_group_name"] = data["deploymentGroupName"]
    if "deploymentConfigName" in data:
        out["deployment_config_name"] = data["deploymentConfigName"]
    if "ec2TagFilters" in data:
        import aws_sdk_codedeploy.types.ec2_tag_filter_list

        out["ec2_tag_filters"] = (
            aws_sdk_codedeploy.types.ec2_tag_filter_list.deserialize_aws_json_1_1(
                data["ec2TagFilters"]
            )
        )
    if "onPremisesInstanceTagFilters" in data:
        import aws_sdk_codedeploy.types.tag_filter_list

        out["on_premises_instance_tag_filters"] = (
            aws_sdk_codedeploy.types.tag_filter_list.deserialize_aws_json_1_1(
                data["onPremisesInstanceTagFilters"]
            )
        )
    if "autoScalingGroups" in data:
        import aws_sdk_codedeploy.types.auto_scaling_group_list

        out["auto_scaling_groups"] = (
            aws_sdk_codedeploy.types.auto_scaling_group_list.deserialize_aws_json_1_1(
                data["autoScalingGroups"]
            )
        )
    if "serviceRoleArn" in data:
        out["service_role_arn"] = data["serviceRoleArn"]
    if "targetRevision" in data:
        import aws_sdk_codedeploy.types.revision_location

        out["target_revision"] = (
            aws_sdk_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["targetRevision"]
            )
        )
    if "triggerConfigurations" in data:
        import aws_sdk_codedeploy.types.trigger_config_list

        out["trigger_configurations"] = (
            aws_sdk_codedeploy.types.trigger_config_list.deserialize_aws_json_1_1(
                data["triggerConfigurations"]
            )
        )
    if "alarmConfiguration" in data:
        import aws_sdk_codedeploy.types.alarm_configuration

        out["alarm_configuration"] = (
            aws_sdk_codedeploy.types.alarm_configuration.deserialize_aws_json_1_1(
                data["alarmConfiguration"]
            )
        )
    if "autoRollbackConfiguration" in data:
        import aws_sdk_codedeploy.types.auto_rollback_configuration

        out["auto_rollback_configuration"] = (
            aws_sdk_codedeploy.types.auto_rollback_configuration.deserialize_aws_json_1_1(
                data["autoRollbackConfiguration"]
            )
        )
    if "deploymentStyle" in data:
        import aws_sdk_codedeploy.types.deployment_style

        out["deployment_style"] = (
            aws_sdk_codedeploy.types.deployment_style.deserialize_aws_json_1_1(
                data["deploymentStyle"]
            )
        )
    if "outdatedInstancesStrategy" in data:
        import aws_sdk_codedeploy.types.outdated_instances_strategy

        out["outdated_instances_strategy"] = (
            aws_sdk_codedeploy.types.outdated_instances_strategy.deserialize_aws_json_1_1(
                data["outdatedInstancesStrategy"]
            )
        )
    if "blueGreenDeploymentConfiguration" in data:
        import aws_sdk_codedeploy.types.blue_green_deployment_configuration

        out["blue_green_deployment_configuration"] = (
            aws_sdk_codedeploy.types.blue_green_deployment_configuration.deserialize_aws_json_1_1(
                data["blueGreenDeploymentConfiguration"]
            )
        )
    if "loadBalancerInfo" in data:
        import aws_sdk_codedeploy.types.load_balancer_info

        out["load_balancer_info"] = (
            aws_sdk_codedeploy.types.load_balancer_info.deserialize_aws_json_1_1(
                data["loadBalancerInfo"]
            )
        )
    if "lastSuccessfulDeployment" in data:
        import aws_sdk_codedeploy.types.last_deployment_info

        out["last_successful_deployment"] = (
            aws_sdk_codedeploy.types.last_deployment_info.deserialize_aws_json_1_1(
                data["lastSuccessfulDeployment"]
            )
        )
    if "lastAttemptedDeployment" in data:
        import aws_sdk_codedeploy.types.last_deployment_info

        out["last_attempted_deployment"] = (
            aws_sdk_codedeploy.types.last_deployment_info.deserialize_aws_json_1_1(
                data["lastAttemptedDeployment"]
            )
        )
    if "ec2TagSet" in data:
        import aws_sdk_codedeploy.types.ec2_tag_set

        out["ec2_tag_set"] = (
            aws_sdk_codedeploy.types.ec2_tag_set.deserialize_aws_json_1_1(
                data["ec2TagSet"]
            )
        )
    if "onPremisesTagSet" in data:
        import aws_sdk_codedeploy.types.on_premises_tag_set

        out["on_premises_tag_set"] = (
            aws_sdk_codedeploy.types.on_premises_tag_set.deserialize_aws_json_1_1(
                data["onPremisesTagSet"]
            )
        )
    if "computePlatform" in data:
        import aws_sdk_codedeploy.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    if "ecsServices" in data:
        import aws_sdk_codedeploy.types.ecs_service_list

        out["ecs_services"] = (
            aws_sdk_codedeploy.types.ecs_service_list.deserialize_aws_json_1_1(
                data["ecsServices"]
            )
        )
    if "terminationHookEnabled" in data:
        out["termination_hook_enabled"] = data["terminationHookEnabled"]
    else:
        out["termination_hook_enabled"] = False
    return out
