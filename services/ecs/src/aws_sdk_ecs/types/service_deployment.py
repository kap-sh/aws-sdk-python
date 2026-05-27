"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeployment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_configuration
    import aws_sdk_ecs.types.deployment_lifecycle_hook_detail_list
    import aws_sdk_ecs.types.rollback
    import aws_sdk_ecs.types.service_deployment_alarms
    import aws_sdk_ecs.types.service_deployment_circuit_breaker
    import aws_sdk_ecs.types.service_deployment_lifecycle_stage
    import aws_sdk_ecs.types.service_deployment_status
    import aws_sdk_ecs.types.service_revision_summary
    import aws_sdk_ecs.types.service_revisions_summary_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ServiceDeployment(TypedDict):
    service_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service deployment.</p>"""
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service for this service deployment.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    finished_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment finished. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the service deployment stopped. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p> <p>The service deployment stops when any of the following actions happen:</p> <ul> <li> <p>A user manually stops the deployment</p> </li> <li> <p>The rollback option is not in use for the failure detection mechanism (the circuit breaker or alarm-based) and the service fails.</p> </li> </ul>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment was last updated. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    source_service_revisions: NotRequired[
        "aws_sdk_ecs.types.service_revisions_summary_list.ServiceRevisionsSummaryList"
    ]
    """<p>The currently deployed workload configuration.</p>"""
    target_service_revision: NotRequired[
        "aws_sdk_ecs.types.service_revision_summary.ServiceRevisionSummary"
    ]
    """<p>The workload configuration being deployed.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.service_deployment_status.ServiceDeploymentStatus"
    ]
    """<p>The service deployment state.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the service deployment is in the current status. For example, the circuit breaker detected a failure.</p>"""
    lifecycle_stage: NotRequired[
        "aws_sdk_ecs.types.service_deployment_lifecycle_stage.ServiceDeploymentLifecycleStage"
    ]
    """<p>The current lifecycle stage of the deployment. Possible values include:</p> <ul> <li> <p>RECONCILE_SERVICE</p> <p>The reconciliation stage that only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state.</p> </li> <li> <p>PRE_SCALE_UP</p> <p>The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic.</p> </li> <li> <p>SCALE_UP</p> <p>The stage when the green service revision scales up to 100% and launches new tasks. The green service revision is not serving any traffic at this point.</p> </li> <li> <p>POST_SCALE_UP</p> <p>The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic.</p> </li> <li> <p>TEST_TRAFFIC_SHIFT</p> <p>The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic.</p> </li> <li> <p>POST_TEST_TRAFFIC_SHIFT</p> <p>The test traffic shift is complete. The green service revision handles 100% of the test traffic.</p> </li> <li> <p>PRODUCTION_TRAFFIC_SHIFT</p> <p>Production traffic is shifting to the green service revision. The green service revision is migrating from 0% to 100% of production traffic.</p> </li> <li> <p>POST_PRODUCTION_TRAFFIC_SHIFT</p> <p>The production traffic shift is complete.</p> </li> <li> <p>BAKE_TIME</p> <p>The stage when both blue and green service revisions are running simultaneously after the production traffic has shifted.</p> </li> <li> <p>CLEAN_UP</p> <p>The stage when the blue service revision has completely scaled down to 0 running tasks. The green service revision is now the production service revision after this stage.</p> </li> </ul>"""
    lifecycle_hook_details: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_detail_list.DeploymentLifecycleHookDetailList"
    ]
    """<p>The details of the lifecycle hooks for the current service deployment.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_ecs.types.deployment_configuration.DeploymentConfiguration"
    ]
    rollback: NotRequired["aws_sdk_ecs.types.rollback.Rollback"]
    """<p>The rollback options the service deployment uses when the deployment fails.</p>"""
    deployment_circuit_breaker: NotRequired[
        "aws_sdk_ecs.types.service_deployment_circuit_breaker.ServiceDeploymentCircuitBreaker"
    ]
    """<p>The circuit breaker configuration that determines a service deployment failed.</p>"""
    alarms: NotRequired[
        "aws_sdk_ecs.types.service_deployment_alarms.ServiceDeploymentAlarms"
    ]
    """<p>The CloudWatch alarms that determine when a service deployment fails.</p>"""
