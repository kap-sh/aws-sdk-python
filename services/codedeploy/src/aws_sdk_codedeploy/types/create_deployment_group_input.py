"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.alarm_configuration
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.auto_rollback_configuration
    import aws_sdk_codedeploy.types.auto_scaling_group_name_list
    import aws_sdk_codedeploy.types.blue_green_deployment_configuration
    import aws_sdk_codedeploy.types.deployment_config_name
    import aws_sdk_codedeploy.types.deployment_group_name
    import aws_sdk_codedeploy.types.deployment_style
    import aws_sdk_codedeploy.types.ec2_tag_filter_list
    import aws_sdk_codedeploy.types.ec2_tag_set
    import aws_sdk_codedeploy.types.ecs_service_list
    import aws_sdk_codedeploy.types.load_balancer_info
    import aws_sdk_codedeploy.types.nullable_boolean
    import aws_sdk_codedeploy.types.on_premises_tag_set
    import aws_sdk_codedeploy.types.outdated_instances_strategy
    import aws_sdk_codedeploy.types.role
    import aws_sdk_codedeploy.types.tag_filter_list
    import aws_sdk_codedeploy.types.tag_list
    import aws_sdk_codedeploy.types.trigger_config_list


class CreateDeploymentGroupInput(TypedDict, closed=True):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    deployment_group_name: (
        "aws_sdk_codedeploy.types.deployment_group_name.DeploymentGroupName"
    )
    """<p>The name of a new deployment group for the specified application.</p>"""
    deployment_config_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    r"""<p>If specified, the deployment configuration name can be either one of the predefined configurations provided with CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.</p> <p> <code>CodeDeployDefault.OneAtATime</code> is the default deployment configuration. It is used if a configuration isn't specified for the deployment or deployment group.</p> <p>For more information about the predefined deployment configurations in CodeDeploy, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html\">Working with Deployment Configurations in CodeDeploy</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    ec2_tag_filters: NotRequired[
        "aws_sdk_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
    ]
    """<p>The Amazon EC2 tags on which to filter. The deployment group includes Amazon EC2 instances with any of the specified tags. Cannot be used in the same call as ec2TagSet.</p>"""
    on_premises_instance_tag_filters: NotRequired[
        "aws_sdk_codedeploy.types.tag_filter_list.TagFilterList"
    ]
    """<p>The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags. Cannot be used in the same call as <code>OnPremisesTagSet</code>.</p>"""
    auto_scaling_groups: NotRequired[
        "aws_sdk_codedeploy.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
    ]
    """<p>A list of associated Amazon EC2 Auto Scaling groups.</p>"""
    service_role_arn: "aws_sdk_codedeploy.types.role.Role"
    """<p>A service role Amazon Resource Name (ARN) that allows CodeDeploy to act on the user's behalf when interacting with Amazon Web Services services.</p>"""
    trigger_configurations: NotRequired[
        "aws_sdk_codedeploy.types.trigger_config_list.TriggerConfigList"
    ]
    r"""<p>Information about triggers to create when the deployment group is created. For examples, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-sns.html\">Create a Trigger for an CodeDeploy Event</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    alarm_configuration: NotRequired[
        "aws_sdk_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>Information to add about Amazon CloudWatch alarms when the deployment group is created.</p>"""
    auto_rollback_configuration: NotRequired[
        "aws_sdk_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Configuration information for an automatic rollback that is added when a deployment group is created.</p>"""
    outdated_instances_strategy: NotRequired[
        "aws_sdk_codedeploy.types.outdated_instances_strategy.OutdatedInstancesStrategy"
    ]
    """<p>Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.</p> <p>If this option is set to <code>UPDATE</code> or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.</p> <p>If this option is set to <code>IGNORE</code>, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.</p>"""
    deployment_style: NotRequired[
        "aws_sdk_codedeploy.types.deployment_style.DeploymentStyle"
    ]
    """<p>Information about the type of deployment, in-place or blue/green, that you want to run and whether to route deployment traffic behind a load balancer.</p>"""
    blue_green_deployment_configuration: NotRequired[
        "aws_sdk_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
    ]
    """<p>Information about blue/green deployment options for a deployment group.</p>"""
    load_balancer_info: NotRequired[
        "aws_sdk_codedeploy.types.load_balancer_info.LoadBalancerInfo"
    ]
    """<p>Information about the load balancer used in a deployment.</p>"""
    ec2_tag_set: NotRequired["aws_sdk_codedeploy.types.ec2_tag_set.EC2TagSet"]
    """<p>Information about groups of tags applied to Amazon EC2 instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same call as <code>ec2TagFilters</code>.</p>"""
    ecs_services: NotRequired[
        "aws_sdk_codedeploy.types.ecs_service_list.ECSServiceList"
    ]
    """<p> The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <code><clustername>:<servicename></code>. </p>"""
    on_premises_tag_set: NotRequired[
        "aws_sdk_codedeploy.types.on_premises_tag_set.OnPremisesTagSet"
    ]
    """<p>Information about groups of tags applied to on-premises instances. The deployment group includes only on-premises instances identified by all of the tag groups. Cannot be used in the same call as <code>onPremisesInstanceTagFilters</code>.</p>"""
    tags: NotRequired["aws_sdk_codedeploy.types.tag_list.TagList"]
    """<p> The metadata that you apply to CodeDeploy deployment groups to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define. </p>"""
    termination_hook_enabled: NotRequired[
        "aws_sdk_codedeploy.types.nullable_boolean.NullableBoolean"
    ]
    r"""<p>This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html\">Integrating CodeDeploy with Amazon EC2 Auto Scaling</a> in the <i>CodeDeploy User Guide</i>.</p> <p>Set <code>terminationHookEnabled</code> to <code>true</code> to have CodeDeploy install a termination hook into your Auto Scaling group when you create a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.</p> <p>For information about termination deployments, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable\">Enabling termination deployments during Auto Scaling scale-in events</a> in the <i>CodeDeploy User Guide</i>.</p> <p>For more information about Auto Scaling scale-in events, see the <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in\">Scale in</a> topic in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentGroupInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
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
        import aws_sdk_codedeploy.types.auto_scaling_group_name_list

        out["autoScalingGroups"] = (
            aws_sdk_codedeploy.types.auto_scaling_group_name_list.serialize_aws_json_1_1(
                value["auto_scaling_groups"]
            )
        )
    out["serviceRoleArn"] = value["service_role_arn"]
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
    if "outdated_instances_strategy" in value:
        import aws_sdk_codedeploy.types.outdated_instances_strategy

        out["outdatedInstancesStrategy"] = (
            aws_sdk_codedeploy.types.outdated_instances_strategy.serialize_aws_json_1_1(
                value["outdated_instances_strategy"]
            )
        )
    if "deployment_style" in value:
        import aws_sdk_codedeploy.types.deployment_style

        out["deploymentStyle"] = (
            aws_sdk_codedeploy.types.deployment_style.serialize_aws_json_1_1(
                value["deployment_style"]
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
    if "ec2_tag_set" in value:
        import aws_sdk_codedeploy.types.ec2_tag_set

        out["ec2TagSet"] = aws_sdk_codedeploy.types.ec2_tag_set.serialize_aws_json_1_1(
            value["ec2_tag_set"]
        )
    if "ecs_services" in value:
        import aws_sdk_codedeploy.types.ecs_service_list

        out["ecsServices"] = (
            aws_sdk_codedeploy.types.ecs_service_list.serialize_aws_json_1_1(
                value["ecs_services"]
            )
        )
    if "on_premises_tag_set" in value:
        import aws_sdk_codedeploy.types.on_premises_tag_set

        out["onPremisesTagSet"] = (
            aws_sdk_codedeploy.types.on_premises_tag_set.serialize_aws_json_1_1(
                value["on_premises_tag_set"]
            )
        )
    if "tags" in value:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "termination_hook_enabled" in value:
        out["terminationHookEnabled"] = value["termination_hook_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentGroupInput:
    out: CreateDeploymentGroupInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "CreateDeploymentGroupInput.application_name required"
        )
    if "deploymentGroupName" in data:
        out["deployment_group_name"] = data["deploymentGroupName"]
    else:
        raise DeserializationError(
            "CreateDeploymentGroupInput.deployment_group_name required"
        )
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
        import aws_sdk_codedeploy.types.auto_scaling_group_name_list

        out["auto_scaling_groups"] = (
            aws_sdk_codedeploy.types.auto_scaling_group_name_list.deserialize_aws_json_1_1(
                data["autoScalingGroups"]
            )
        )
    if "serviceRoleArn" in data:
        out["service_role_arn"] = data["serviceRoleArn"]
    else:
        raise DeserializationError(
            "CreateDeploymentGroupInput.service_role_arn required"
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
    if "outdatedInstancesStrategy" in data:
        import aws_sdk_codedeploy.types.outdated_instances_strategy

        out["outdated_instances_strategy"] = (
            aws_sdk_codedeploy.types.outdated_instances_strategy.deserialize_aws_json_1_1(
                data["outdatedInstancesStrategy"]
            )
        )
    if "deploymentStyle" in data:
        import aws_sdk_codedeploy.types.deployment_style

        out["deployment_style"] = (
            aws_sdk_codedeploy.types.deployment_style.deserialize_aws_json_1_1(
                data["deploymentStyle"]
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
    if "ec2TagSet" in data:
        import aws_sdk_codedeploy.types.ec2_tag_set

        out["ec2_tag_set"] = (
            aws_sdk_codedeploy.types.ec2_tag_set.deserialize_aws_json_1_1(
                data["ec2TagSet"]
            )
        )
    if "ecsServices" in data:
        import aws_sdk_codedeploy.types.ecs_service_list

        out["ecs_services"] = (
            aws_sdk_codedeploy.types.ecs_service_list.deserialize_aws_json_1_1(
                data["ecsServices"]
            )
        )
    if "onPremisesTagSet" in data:
        import aws_sdk_codedeploy.types.on_premises_tag_set

        out["on_premises_tag_set"] = (
            aws_sdk_codedeploy.types.on_premises_tag_set.deserialize_aws_json_1_1(
                data["onPremisesTagSet"]
            )
        )
    if "tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "terminationHookEnabled" in data:
        out["termination_hook_enabled"] = data["terminationHookEnabled"]
    return out
