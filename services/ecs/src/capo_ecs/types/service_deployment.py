"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.deployment_configuration
    import capo_ecs.types.deployment_lifecycle_hook_detail_list
    import capo_ecs.types.rollback
    import capo_ecs.types.service_deployment_alarms
    import capo_ecs.types.service_deployment_circuit_breaker
    import capo_ecs.types.service_deployment_lifecycle_stage
    import capo_ecs.types.service_deployment_status
    import capo_ecs.types.service_revision_summary
    import capo_ecs.types.service_revisions_summary_list
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ServiceDeployment(TypedDict, closed=True):
    service_deployment_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service deployment.</p>"""
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service for this service deployment.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    started_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    finished_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment finished. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    stopped_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment stopped. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p> <p>The service deployment stops when any of the following actions happen:</p> <ul> <li> <p>A user manually stops the deployment</p> </li> <li> <p>The rollback option is not in use for the failure detection mechanism (the circuit breaker or alarm-based) and the service fails.</p> </li> </ul>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment was last updated. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    source_service_revisions: NotRequired[
        "capo_ecs.types.service_revisions_summary_list.ServiceRevisionsSummaryList"
    ]
    """<p>The currently deployed workload configuration.</p>"""
    target_service_revision: NotRequired[
        "capo_ecs.types.service_revision_summary.ServiceRevisionSummary"
    ]
    """<p>The workload configuration being deployed.</p>"""
    status: NotRequired[
        "capo_ecs.types.service_deployment_status.ServiceDeploymentStatus"
    ]
    """<p>The service deployment state.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the service deployment is in the current status. For example, the circuit breaker detected a failure.</p>"""
    lifecycle_stage: NotRequired[
        "capo_ecs.types.service_deployment_lifecycle_stage.ServiceDeploymentLifecycleStage"
    ]
    """<p>The current lifecycle stage of the deployment. Possible values include:</p> <ul> <li> <p>RECONCILE_SERVICE</p> <p>The reconciliation stage that only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state.</p> </li> <li> <p>PRE_SCALE_UP</p> <p>The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic.</p> </li> <li> <p>SCALE_UP</p> <p>The stage when the green service revision scales up to 100% and launches new tasks. The green service revision is not serving any traffic at this point.</p> </li> <li> <p>POST_SCALE_UP</p> <p>The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic.</p> </li> <li> <p>TEST_TRAFFIC_SHIFT</p> <p>The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic.</p> </li> <li> <p>POST_TEST_TRAFFIC_SHIFT</p> <p>The test traffic shift is complete. The green service revision handles 100% of the test traffic.</p> </li> <li> <p>PRODUCTION_TRAFFIC_SHIFT</p> <p>Production traffic is shifting to the green service revision. The green service revision is migrating from 0% to 100% of production traffic.</p> </li> <li> <p>POST_PRODUCTION_TRAFFIC_SHIFT</p> <p>The production traffic shift is complete.</p> </li> <li> <p>BAKE_TIME</p> <p>The stage when both blue and green service revisions are running simultaneously after the production traffic has shifted.</p> </li> <li> <p>CLEAN_UP</p> <p>The stage when the blue service revision has completely scaled down to 0 running tasks. The green service revision is now the production service revision after this stage.</p> </li> </ul>"""
    lifecycle_hook_details: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_detail_list.DeploymentLifecycleHookDetailList"
    ]
    """<p>The details of the lifecycle hooks for the current service deployment.</p>"""
    deployment_configuration: NotRequired[
        "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
    ]
    rollback: NotRequired["capo_ecs.types.rollback.Rollback"]
    """<p>The rollback options the service deployment uses when the deployment fails.</p>"""
    deployment_circuit_breaker: NotRequired[
        "capo_ecs.types.service_deployment_circuit_breaker.ServiceDeploymentCircuitBreaker"
    ]
    """<p>The circuit breaker configuration that determines a service deployment failed.</p>"""
    alarms: NotRequired[
        "capo_ecs.types.service_deployment_alarms.ServiceDeploymentAlarms"
    ]
    """<p>The CloudWatch alarms that determine when a service deployment fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeployment) -> dict:
    out: dict = {}
    if "service_deployment_arn" in value:
        out["serviceDeploymentArn"] = value["service_deployment_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "started_at" in value:
        import capo_ecs.types.timestamp

        out["startedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "finished_at" in value:
        import capo_ecs.types.timestamp

        out["finishedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["finished_at"]
        )
    if "stopped_at" in value:
        import capo_ecs.types.timestamp

        out["stoppedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["stopped_at"]
        )
    if "updated_at" in value:
        import capo_ecs.types.timestamp

        out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "source_service_revisions" in value:
        import capo_ecs.types.service_revisions_summary_list

        out["sourceServiceRevisions"] = (
            capo_ecs.types.service_revisions_summary_list.serialize_aws_json_1_1(
                value["source_service_revisions"]
            )
        )
    if "target_service_revision" in value:
        import capo_ecs.types.service_revision_summary

        out["targetServiceRevision"] = (
            capo_ecs.types.service_revision_summary.serialize_aws_json_1_1(
                value["target_service_revision"]
            )
        )
    if "status" in value:
        import capo_ecs.types.service_deployment_status

        out["status"] = capo_ecs.types.service_deployment_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "lifecycle_stage" in value:
        import capo_ecs.types.service_deployment_lifecycle_stage

        out["lifecycleStage"] = (
            capo_ecs.types.service_deployment_lifecycle_stage.serialize_aws_json_1_1(
                value["lifecycle_stage"]
            )
        )
    if "lifecycle_hook_details" in value:
        import capo_ecs.types.deployment_lifecycle_hook_detail_list

        out["lifecycleHookDetails"] = (
            capo_ecs.types.deployment_lifecycle_hook_detail_list.serialize_aws_json_1_1(
                value["lifecycle_hook_details"]
            )
        )
    if "deployment_configuration" in value:
        import capo_ecs.types.deployment_configuration

        out["deploymentConfiguration"] = (
            capo_ecs.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "rollback" in value:
        import capo_ecs.types.rollback

        out["rollback"] = capo_ecs.types.rollback.serialize_aws_json_1_1(
            value["rollback"]
        )
    if "deployment_circuit_breaker" in value:
        import capo_ecs.types.service_deployment_circuit_breaker

        out["deploymentCircuitBreaker"] = (
            capo_ecs.types.service_deployment_circuit_breaker.serialize_aws_json_1_1(
                value["deployment_circuit_breaker"]
            )
        )
    if "alarms" in value:
        import capo_ecs.types.service_deployment_alarms

        out["alarms"] = capo_ecs.types.service_deployment_alarms.serialize_aws_json_1_1(
            value["alarms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceDeployment:
    out: ServiceDeployment = {}  # type: ignore[typeddict-item]
    if "serviceDeploymentArn" in data:
        out["service_deployment_arn"] = data["serviceDeploymentArn"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "createdAt" in data:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "startedAt" in data:
        import capo_ecs.types.timestamp

        out["started_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if "finishedAt" in data:
        import capo_ecs.types.timestamp

        out["finished_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["finishedAt"]
        )
    if "stoppedAt" in data:
        import capo_ecs.types.timestamp

        out["stopped_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["stoppedAt"]
        )
    if "updatedAt" in data:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    if "sourceServiceRevisions" in data:
        import capo_ecs.types.service_revisions_summary_list

        out["source_service_revisions"] = (
            capo_ecs.types.service_revisions_summary_list.deserialize_aws_json_1_1(
                data["sourceServiceRevisions"]
            )
        )
    if "targetServiceRevision" in data:
        import capo_ecs.types.service_revision_summary

        out["target_service_revision"] = (
            capo_ecs.types.service_revision_summary.deserialize_aws_json_1_1(
                data["targetServiceRevision"]
            )
        )
    if "status" in data:
        import capo_ecs.types.service_deployment_status

        out["status"] = (
            capo_ecs.types.service_deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lifecycleStage" in data:
        import capo_ecs.types.service_deployment_lifecycle_stage

        out["lifecycle_stage"] = (
            capo_ecs.types.service_deployment_lifecycle_stage.deserialize_aws_json_1_1(
                data["lifecycleStage"]
            )
        )
    if "lifecycleHookDetails" in data:
        import capo_ecs.types.deployment_lifecycle_hook_detail_list

        out["lifecycle_hook_details"] = (
            capo_ecs.types.deployment_lifecycle_hook_detail_list.deserialize_aws_json_1_1(
                data["lifecycleHookDetails"]
            )
        )
    if "deploymentConfiguration" in data:
        import capo_ecs.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_ecs.types.deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
    if "rollback" in data:
        import capo_ecs.types.rollback

        out["rollback"] = capo_ecs.types.rollback.deserialize_aws_json_1_1(
            data["rollback"]
        )
    if "deploymentCircuitBreaker" in data:
        import capo_ecs.types.service_deployment_circuit_breaker

        out["deployment_circuit_breaker"] = (
            capo_ecs.types.service_deployment_circuit_breaker.deserialize_aws_json_1_1(
                data["deploymentCircuitBreaker"]
            )
        )
    if "alarms" in data:
        import capo_ecs.types.service_deployment_alarms

        out["alarms"] = (
            capo_ecs.types.service_deployment_alarms.deserialize_aws_json_1_1(
                data["alarms"]
            )
        )
    return out
