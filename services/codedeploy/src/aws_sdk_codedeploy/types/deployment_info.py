"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.additional_deployment_status_info
    import aws_sdk_codedeploy.types.alarm_configuration
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.auto_rollback_configuration
    import aws_sdk_codedeploy.types.blue_green_deployment_configuration
    import aws_sdk_codedeploy.types.boolean
    import aws_sdk_codedeploy.types.compute_platform
    import aws_sdk_codedeploy.types.deployment_config_name
    import aws_sdk_codedeploy.types.deployment_creator
    import aws_sdk_codedeploy.types.deployment_group_name
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.deployment_overview
    import aws_sdk_codedeploy.types.deployment_status
    import aws_sdk_codedeploy.types.deployment_status_message_list
    import aws_sdk_codedeploy.types.deployment_style
    import aws_sdk_codedeploy.types.description
    import aws_sdk_codedeploy.types.error_information
    import aws_sdk_codedeploy.types.external_id
    import aws_sdk_codedeploy.types.file_exists_behavior
    import aws_sdk_codedeploy.types.load_balancer_info
    import aws_sdk_codedeploy.types.related_deployments
    import aws_sdk_codedeploy.types.revision_location
    import aws_sdk_codedeploy.types.rollback_info
    import aws_sdk_codedeploy.types.target_instances
    import aws_sdk_codedeploy.types.timestamp


class DeploymentInfo(TypedDict):
    application_name: NotRequired[
        "aws_sdk_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The application name.</p>"""
    deployment_group_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_name.DeploymentGroupName"
    ]
    """<p> The deployment group name. </p>"""
    deployment_config_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p> The deployment configuration name. </p>"""
    deployment_id: NotRequired["aws_sdk_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    previous_revision: NotRequired[
        "aws_sdk_codedeploy.types.revision_location.RevisionLocation"
    ]
    """<p>Information about the application revision that was deployed to the deployment group before the most recent successful deployment.</p>"""
    revision: NotRequired["aws_sdk_codedeploy.types.revision_location.RevisionLocation"]
    """<p>Information about the location of stored application artifacts and the service from which to retrieve them.</p>"""
    status: NotRequired["aws_sdk_codedeploy.types.deployment_status.DeploymentStatus"]
    """<p>The current state of the deployment as a whole.</p>"""
    error_information: NotRequired[
        "aws_sdk_codedeploy.types.error_information.ErrorInformation"
    ]
    """<p>Information about any error associated with this deployment.</p>"""
    create_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment was created.</p>"""
    start_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment was deployed to the deployment group.</p> <p>In some cases, the reported value of the start time might be later than the complete time. This is due to differences in the clock settings of backend servers that participate in the deployment process.</p>"""
    complete_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment was complete.</p>"""
    deployment_overview: NotRequired[
        "aws_sdk_codedeploy.types.deployment_overview.DeploymentOverview"
    ]
    """<p>A summary of the deployment status of the instances in the deployment.</p>"""
    description: NotRequired["aws_sdk_codedeploy.types.description.Description"]
    """<p>A comment about the deployment.</p>"""
    creator: NotRequired[
        "aws_sdk_codedeploy.types.deployment_creator.DeploymentCreator"
    ]
    """<p>The means by which the deployment was created:</p> <ul> <li> <p> <code>user</code>: A user created the deployment.</p> </li> <li> <p> <code>autoscaling</code>: Amazon EC2 Auto Scaling created the deployment.</p> </li> <li> <p> <code>codeDeployRollback</code>: A rollback process created the deployment.</p> </li> <li> <p> <code>CodeDeployAutoUpdate</code>: An auto-update process created the deployment when it detected outdated Amazon EC2 instances.</p> </li> </ul>"""
    ignore_application_stop_failures: "aws_sdk_codedeploy.types.boolean.Boolean"
    """<p> If true, then if an <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, or <code>AfterBlockTraffic</code> deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if <code>ApplicationStop</code> fails, the deployment continues with DownloadBundle. If <code>BeforeBlockTraffic</code> fails, the deployment continues with <code>BlockTraffic</code>. If <code>AfterBlockTraffic</code> fails, the deployment continues with <code>ApplicationStop</code>. </p> <p> If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted. </p> <p> During a deployment, the CodeDeploy agent runs the scripts specified for <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail. </p> <p> If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use <code>ignoreApplicationStopFailures</code> to specify that the <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> failures should be ignored. </p>"""
    auto_rollback_configuration: NotRequired[
        "aws_sdk_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Information about the automatic rollback configuration associated with the deployment.</p>"""
    update_outdated_instances_only: "aws_sdk_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether only instances that are not running the latest application revision are to be deployed to.</p>"""
    rollback_info: NotRequired["aws_sdk_codedeploy.types.rollback_info.RollbackInfo"]
    """<p>Information about a deployment rollback.</p>"""
    deployment_style: NotRequired[
        "aws_sdk_codedeploy.types.deployment_style.DeploymentStyle"
    ]
    """<p>Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.</p>"""
    target_instances: NotRequired[
        "aws_sdk_codedeploy.types.target_instances.TargetInstances"
    ]
    """<p>Information about the instances that belong to the replacement environment in a blue/green deployment.</p>"""
    instance_termination_wait_time_started: "aws_sdk_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether the wait period set for the termination of instances in the original environment has started. Status is 'false' if the KEEP_ALIVE option is specified. Otherwise, 'true' as soon as the termination wait period starts.</p>"""
    blue_green_deployment_configuration: NotRequired[
        "aws_sdk_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
    ]
    """<p>Information about blue/green deployment options for this deployment.</p>"""
    load_balancer_info: NotRequired[
        "aws_sdk_codedeploy.types.load_balancer_info.LoadBalancerInfo"
    ]
    """<p>Information about the load balancer used in the deployment.</p>"""
    additional_deployment_status_info: NotRequired[
        "aws_sdk_codedeploy.types.additional_deployment_status_info.AdditionalDeploymentStatusInfo"
    ]
    """<p>Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.</p>"""
    file_exists_behavior: NotRequired[
        "aws_sdk_codedeploy.types.file_exists_behavior.FileExistsBehavior"
    ]
    """<p>Information about how CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.</p> <ul> <li> <p> <code>DISALLOW</code>: The deployment fails. This is also the default behavior if no option is specified.</p> </li> <li> <p> <code>OVERWRITE</code>: The version of the file from the application revision currently being deployed replaces the version already on the instance.</p> </li> <li> <p> <code>RETAIN</code>: The version of the file already on the instance is kept and used as part of the new deployment.</p> </li> </ul>"""
    deployment_status_messages: NotRequired[
        "aws_sdk_codedeploy.types.deployment_status_message_list.DeploymentStatusMessageList"
    ]
    """<p>Messages that contain information about the status of a deployment.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>"""
    external_id: NotRequired["aws_sdk_codedeploy.types.external_id.ExternalId"]
    """<p>The unique ID for an external resource (for example, a CloudFormation stack ID) that is linked to this deployment.</p>"""
    related_deployments: NotRequired[
        "aws_sdk_codedeploy.types.related_deployments.RelatedDeployments"
    ]
    override_alarm_configuration: NotRequired[
        "aws_sdk_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentInfo) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "deployment_group_name" in value:
        out["deploymentGroupName"] = value["deployment_group_name"]
    if "deployment_config_name" in value:
        out["deploymentConfigName"] = value["deployment_config_name"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "previous_revision" in value:
        import aws_sdk_codedeploy.types.revision_location

        out["previousRevision"] = (
            aws_sdk_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["previous_revision"]
            )
        )
    if "revision" in value:
        import aws_sdk_codedeploy.types.revision_location

        out["revision"] = (
            aws_sdk_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["revision"]
            )
        )
    if "status" in value:
        import aws_sdk_codedeploy.types.deployment_status

        out["status"] = (
            aws_sdk_codedeploy.types.deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_information" in value:
        import aws_sdk_codedeploy.types.error_information

        out["errorInformation"] = (
            aws_sdk_codedeploy.types.error_information.serialize_aws_json_1_1(
                value["error_information"]
            )
        )
    if "create_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["createTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "start_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["startTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "complete_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["completeTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["complete_time"]
        )
    if "deployment_overview" in value:
        import aws_sdk_codedeploy.types.deployment_overview

        out["deploymentOverview"] = (
            aws_sdk_codedeploy.types.deployment_overview.serialize_aws_json_1_1(
                value["deployment_overview"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "creator" in value:
        import aws_sdk_codedeploy.types.deployment_creator

        out["creator"] = (
            aws_sdk_codedeploy.types.deployment_creator.serialize_aws_json_1_1(
                value["creator"]
            )
        )
    out["ignoreApplicationStopFailures"] = value.get(
        "ignore_application_stop_failures", False
    )
    if "auto_rollback_configuration" in value:
        import aws_sdk_codedeploy.types.auto_rollback_configuration

        out["autoRollbackConfiguration"] = (
            aws_sdk_codedeploy.types.auto_rollback_configuration.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    out["updateOutdatedInstancesOnly"] = value.get(
        "update_outdated_instances_only", False
    )
    if "rollback_info" in value:
        import aws_sdk_codedeploy.types.rollback_info

        out["rollbackInfo"] = (
            aws_sdk_codedeploy.types.rollback_info.serialize_aws_json_1_1(
                value["rollback_info"]
            )
        )
    if "deployment_style" in value:
        import aws_sdk_codedeploy.types.deployment_style

        out["deploymentStyle"] = (
            aws_sdk_codedeploy.types.deployment_style.serialize_aws_json_1_1(
                value["deployment_style"]
            )
        )
    if "target_instances" in value:
        import aws_sdk_codedeploy.types.target_instances

        out["targetInstances"] = (
            aws_sdk_codedeploy.types.target_instances.serialize_aws_json_1_1(
                value["target_instances"]
            )
        )
    out["instanceTerminationWaitTimeStarted"] = value.get(
        "instance_termination_wait_time_started", False
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
    if "additional_deployment_status_info" in value:
        out["additionalDeploymentStatusInfo"] = value[
            "additional_deployment_status_info"
        ]
    if "file_exists_behavior" in value:
        import aws_sdk_codedeploy.types.file_exists_behavior

        out["fileExistsBehavior"] = (
            aws_sdk_codedeploy.types.file_exists_behavior.serialize_aws_json_1_1(
                value["file_exists_behavior"]
            )
        )
    if "deployment_status_messages" in value:
        import aws_sdk_codedeploy.types.deployment_status_message_list

        out["deploymentStatusMessages"] = (
            aws_sdk_codedeploy.types.deployment_status_message_list.serialize_aws_json_1_1(
                value["deployment_status_messages"]
            )
        )
    if "compute_platform" in value:
        import aws_sdk_codedeploy.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "related_deployments" in value:
        import aws_sdk_codedeploy.types.related_deployments

        out["relatedDeployments"] = (
            aws_sdk_codedeploy.types.related_deployments.serialize_aws_json_1_1(
                value["related_deployments"]
            )
        )
    if "override_alarm_configuration" in value:
        import aws_sdk_codedeploy.types.alarm_configuration

        out["overrideAlarmConfiguration"] = (
            aws_sdk_codedeploy.types.alarm_configuration.serialize_aws_json_1_1(
                value["override_alarm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentInfo:
    out: DeploymentInfo = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "deploymentGroupName" in data:
        out["deployment_group_name"] = data["deploymentGroupName"]
    if "deploymentConfigName" in data:
        out["deployment_config_name"] = data["deploymentConfigName"]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "previousRevision" in data:
        import aws_sdk_codedeploy.types.revision_location

        out["previous_revision"] = (
            aws_sdk_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["previousRevision"]
            )
        )
    if "revision" in data:
        import aws_sdk_codedeploy.types.revision_location

        out["revision"] = (
            aws_sdk_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revision"]
            )
        )
    if "status" in data:
        import aws_sdk_codedeploy.types.deployment_status

        out["status"] = (
            aws_sdk_codedeploy.types.deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "errorInformation" in data:
        import aws_sdk_codedeploy.types.error_information

        out["error_information"] = (
            aws_sdk_codedeploy.types.error_information.deserialize_aws_json_1_1(
                data["errorInformation"]
            )
        )
    if "createTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["create_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["createTime"]
            )
        )
    if "startTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["start_time"] = aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "completeTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["complete_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["completeTime"]
            )
        )
    if "deploymentOverview" in data:
        import aws_sdk_codedeploy.types.deployment_overview

        out["deployment_overview"] = (
            aws_sdk_codedeploy.types.deployment_overview.deserialize_aws_json_1_1(
                data["deploymentOverview"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "creator" in data:
        import aws_sdk_codedeploy.types.deployment_creator

        out["creator"] = (
            aws_sdk_codedeploy.types.deployment_creator.deserialize_aws_json_1_1(
                data["creator"]
            )
        )
    if "ignoreApplicationStopFailures" in data:
        out["ignore_application_stop_failures"] = data["ignoreApplicationStopFailures"]
    else:
        out["ignore_application_stop_failures"] = False
    if "autoRollbackConfiguration" in data:
        import aws_sdk_codedeploy.types.auto_rollback_configuration

        out["auto_rollback_configuration"] = (
            aws_sdk_codedeploy.types.auto_rollback_configuration.deserialize_aws_json_1_1(
                data["autoRollbackConfiguration"]
            )
        )
    if "updateOutdatedInstancesOnly" in data:
        out["update_outdated_instances_only"] = data["updateOutdatedInstancesOnly"]
    else:
        out["update_outdated_instances_only"] = False
    if "rollbackInfo" in data:
        import aws_sdk_codedeploy.types.rollback_info

        out["rollback_info"] = (
            aws_sdk_codedeploy.types.rollback_info.deserialize_aws_json_1_1(
                data["rollbackInfo"]
            )
        )
    if "deploymentStyle" in data:
        import aws_sdk_codedeploy.types.deployment_style

        out["deployment_style"] = (
            aws_sdk_codedeploy.types.deployment_style.deserialize_aws_json_1_1(
                data["deploymentStyle"]
            )
        )
    if "targetInstances" in data:
        import aws_sdk_codedeploy.types.target_instances

        out["target_instances"] = (
            aws_sdk_codedeploy.types.target_instances.deserialize_aws_json_1_1(
                data["targetInstances"]
            )
        )
    if "instanceTerminationWaitTimeStarted" in data:
        out["instance_termination_wait_time_started"] = data[
            "instanceTerminationWaitTimeStarted"
        ]
    else:
        out["instance_termination_wait_time_started"] = False
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
    if "additionalDeploymentStatusInfo" in data:
        out["additional_deployment_status_info"] = data[
            "additionalDeploymentStatusInfo"
        ]
    if "fileExistsBehavior" in data:
        import aws_sdk_codedeploy.types.file_exists_behavior

        out["file_exists_behavior"] = (
            aws_sdk_codedeploy.types.file_exists_behavior.deserialize_aws_json_1_1(
                data["fileExistsBehavior"]
            )
        )
    if "deploymentStatusMessages" in data:
        import aws_sdk_codedeploy.types.deployment_status_message_list

        out["deployment_status_messages"] = (
            aws_sdk_codedeploy.types.deployment_status_message_list.deserialize_aws_json_1_1(
                data["deploymentStatusMessages"]
            )
        )
    if "computePlatform" in data:
        import aws_sdk_codedeploy.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "relatedDeployments" in data:
        import aws_sdk_codedeploy.types.related_deployments

        out["related_deployments"] = (
            aws_sdk_codedeploy.types.related_deployments.deserialize_aws_json_1_1(
                data["relatedDeployments"]
            )
        )
    if "overrideAlarmConfiguration" in data:
        import aws_sdk_codedeploy.types.alarm_configuration

        out["override_alarm_configuration"] = (
            aws_sdk_codedeploy.types.alarm_configuration.deserialize_aws_json_1_1(
                data["overrideAlarmConfiguration"]
            )
        )
    return out
