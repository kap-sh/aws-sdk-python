"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Observation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.cloud_watch_event_detail_type
    import aws_sdk_application_insights.types.cloud_watch_event_id
    import aws_sdk_application_insights.types.cloud_watch_event_source
    import aws_sdk_application_insights.types.code_deploy_application
    import aws_sdk_application_insights.types.code_deploy_deployment_group
    import aws_sdk_application_insights.types.code_deploy_deployment_id
    import aws_sdk_application_insights.types.code_deploy_instance_group_id
    import aws_sdk_application_insights.types.code_deploy_state
    import aws_sdk_application_insights.types.ebs_cause
    import aws_sdk_application_insights.types.ebs_event
    import aws_sdk_application_insights.types.ebs_request_id
    import aws_sdk_application_insights.types.ebs_result
    import aws_sdk_application_insights.types.ec2_state
    import aws_sdk_application_insights.types.end_time
    import aws_sdk_application_insights.types.health_event_arn
    import aws_sdk_application_insights.types.health_event_description
    import aws_sdk_application_insights.types.health_event_type_category
    import aws_sdk_application_insights.types.health_event_type_code
    import aws_sdk_application_insights.types.health_service
    import aws_sdk_application_insights.types.line_time
    import aws_sdk_application_insights.types.log_filter
    import aws_sdk_application_insights.types.log_group
    import aws_sdk_application_insights.types.log_text
    import aws_sdk_application_insights.types.metric_name
    import aws_sdk_application_insights.types.metric_namespace
    import aws_sdk_application_insights.types.observation_id
    import aws_sdk_application_insights.types.rds_event_categories
    import aws_sdk_application_insights.types.rds_event_message
    import aws_sdk_application_insights.types.s3_event_name
    import aws_sdk_application_insights.types.source_arn
    import aws_sdk_application_insights.types.source_type
    import aws_sdk_application_insights.types.start_time
    import aws_sdk_application_insights.types.states_arn
    import aws_sdk_application_insights.types.states_execution_arn
    import aws_sdk_application_insights.types.states_input
    import aws_sdk_application_insights.types.states_status
    import aws_sdk_application_insights.types.unit
    import aws_sdk_application_insights.types.value
    import aws_sdk_application_insights.types.x_ray_error_percent
    import aws_sdk_application_insights.types.x_ray_fault_percent
    import aws_sdk_application_insights.types.x_ray_node_name
    import aws_sdk_application_insights.types.x_ray_node_type
    import aws_sdk_application_insights.types.x_ray_request_average_latency
    import aws_sdk_application_insights.types.x_ray_request_count
    import aws_sdk_application_insights.types.x_ray_throttle_percent


class Observation(TypedDict, closed=True):
    id: NotRequired["aws_sdk_application_insights.types.observation_id.ObservationId"]
    """<p>The ID of the observation type.</p>"""
    start_time: NotRequired["aws_sdk_application_insights.types.start_time.StartTime"]
    """<p>The time when the observation was first detected, in epoch seconds.</p>"""
    end_time: NotRequired["aws_sdk_application_insights.types.end_time.EndTime"]
    """<p>The time when the observation ended, in epoch seconds.</p>"""
    source_type: NotRequired[
        "aws_sdk_application_insights.types.source_type.SourceType"
    ]
    """<p>The source type of the observation.</p>"""
    source_arn: NotRequired["aws_sdk_application_insights.types.source_arn.SourceARN"]
    """<p>The source resource ARN of the observation.</p>"""
    log_group: NotRequired["aws_sdk_application_insights.types.log_group.LogGroup"]
    """<p>The log group name.</p>"""
    line_time: NotRequired["aws_sdk_application_insights.types.line_time.LineTime"]
    """<p>The timestamp in the CloudWatch Logs that specifies when the matched line occurred.</p>"""
    log_text: NotRequired["aws_sdk_application_insights.types.log_text.LogText"]
    """<p>The log text of the observation.</p>"""
    log_filter: NotRequired["aws_sdk_application_insights.types.log_filter.LogFilter"]
    """<p>The log filter of the observation.</p>"""
    metric_namespace: NotRequired[
        "aws_sdk_application_insights.types.metric_namespace.MetricNamespace"
    ]
    """<p>The namespace of the observation metric.</p>"""
    metric_name: NotRequired[
        "aws_sdk_application_insights.types.metric_name.MetricName"
    ]
    """<p>The name of the observation metric.</p>"""
    unit: NotRequired["aws_sdk_application_insights.types.unit.Unit"]
    """<p>The unit of the source observation metric.</p>"""
    value: NotRequired["aws_sdk_application_insights.types.value.Value"]
    """<p>The value of the source observation metric.</p>"""
    cloud_watch_event_id: NotRequired[
        "aws_sdk_application_insights.types.cloud_watch_event_id.CloudWatchEventId"
    ]
    """<p> The ID of the CloudWatch Event-based observation related to the detected problem. </p>"""
    cloud_watch_event_source: NotRequired[
        "aws_sdk_application_insights.types.cloud_watch_event_source.CloudWatchEventSource"
    ]
    """<p> The source of the CloudWatch Event. </p>"""
    cloud_watch_event_detail_type: NotRequired[
        "aws_sdk_application_insights.types.cloud_watch_event_detail_type.CloudWatchEventDetailType"
    ]
    """<p> The detail type of the CloudWatch Event-based observation, for example, <code>EC2 Instance State-change Notification</code>. </p>"""
    health_event_arn: NotRequired[
        "aws_sdk_application_insights.types.health_event_arn.HealthEventArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the Health Event-based observation.</p>"""
    health_service: NotRequired[
        "aws_sdk_application_insights.types.health_service.HealthService"
    ]
    """<p> The service to which the Health Event belongs, such as EC2. </p>"""
    health_event_type_code: NotRequired[
        "aws_sdk_application_insights.types.health_event_type_code.HealthEventTypeCode"
    ]
    """<p> The type of the Health event, for example, <code>AWS_EC2_POWER_CONNECTIVITY_ISSUE</code>. </p>"""
    health_event_type_category: NotRequired[
        "aws_sdk_application_insights.types.health_event_type_category.HealthEventTypeCategory"
    ]
    """<p> The category of the Health event, such as <code>issue</code>. </p>"""
    health_event_description: NotRequired[
        "aws_sdk_application_insights.types.health_event_description.HealthEventDescription"
    ]
    """<p> The description of the Health event provided by the service, such as Amazon EC2. </p>"""
    code_deploy_deployment_id: NotRequired[
        "aws_sdk_application_insights.types.code_deploy_deployment_id.CodeDeployDeploymentId"
    ]
    """<p> The deployment ID of the CodeDeploy-based observation related to the detected problem. </p>"""
    code_deploy_deployment_group: NotRequired[
        "aws_sdk_application_insights.types.code_deploy_deployment_group.CodeDeployDeploymentGroup"
    ]
    """<p> The deployment group to which the CodeDeploy deployment belongs. </p>"""
    code_deploy_state: NotRequired[
        "aws_sdk_application_insights.types.code_deploy_state.CodeDeployState"
    ]
    """<p> The status of the CodeDeploy deployment, for example <code>SUCCESS</code> or <code> FAILURE</code>. </p>"""
    code_deploy_application: NotRequired[
        "aws_sdk_application_insights.types.code_deploy_application.CodeDeployApplication"
    ]
    """<p> The CodeDeploy application to which the deployment belongs. </p>"""
    code_deploy_instance_group_id: NotRequired[
        "aws_sdk_application_insights.types.code_deploy_instance_group_id.CodeDeployInstanceGroupId"
    ]
    """<p> The instance group to which the CodeDeploy instance belongs. </p>"""
    ec2_state: NotRequired["aws_sdk_application_insights.types.ec2_state.Ec2State"]
    """<p> The state of the instance, such as <code>STOPPING</code> or <code>TERMINATING</code>. </p>"""
    rds_event_categories: NotRequired[
        "aws_sdk_application_insights.types.rds_event_categories.RdsEventCategories"
    ]
    """<p> The category of an RDS event. </p>"""
    rds_event_message: NotRequired[
        "aws_sdk_application_insights.types.rds_event_message.RdsEventMessage"
    ]
    """<p> The message of an RDS event. </p>"""
    s3_event_name: NotRequired[
        "aws_sdk_application_insights.types.s3_event_name.S3EventName"
    ]
    """<p> The name of the S3 CloudWatch Event-based observation. </p>"""
    states_execution_arn: NotRequired[
        "aws_sdk_application_insights.types.states_execution_arn.StatesExecutionArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the step function execution-based observation. </p>"""
    states_arn: NotRequired["aws_sdk_application_insights.types.states_arn.StatesArn"]
    """<p> The Amazon Resource Name (ARN) of the step function-based observation. </p>"""
    states_status: NotRequired[
        "aws_sdk_application_insights.types.states_status.StatesStatus"
    ]
    """<p> The status of the step function-related observation. </p>"""
    states_input: NotRequired[
        "aws_sdk_application_insights.types.states_input.StatesInput"
    ]
    """<p> The input to the step function-based observation. </p>"""
    ebs_event: NotRequired["aws_sdk_application_insights.types.ebs_event.EbsEvent"]
    """<p> The type of EBS CloudWatch event, such as <code>createVolume</code>, <code>deleteVolume</code> or <code>attachVolume</code>. </p>"""
    ebs_result: NotRequired["aws_sdk_application_insights.types.ebs_result.EbsResult"]
    """<p> The result of an EBS CloudWatch event, such as <code>failed</code> or <code>succeeded</code>. </p>"""
    ebs_cause: NotRequired["aws_sdk_application_insights.types.ebs_cause.EbsCause"]
    """<p> The cause of an EBS CloudWatch event. </p>"""
    ebs_request_id: NotRequired[
        "aws_sdk_application_insights.types.ebs_request_id.EbsRequestId"
    ]
    """<p> The request ID of an EBS CloudWatch event. </p>"""
    x_ray_fault_percent: NotRequired[
        "aws_sdk_application_insights.types.x_ray_fault_percent.XRayFaultPercent"
    ]
    """<p> The X-Ray request fault percentage for this node. </p>"""
    x_ray_throttle_percent: NotRequired[
        "aws_sdk_application_insights.types.x_ray_throttle_percent.XRayThrottlePercent"
    ]
    """<p> The X-Ray request throttle percentage for this node. </p>"""
    x_ray_error_percent: NotRequired[
        "aws_sdk_application_insights.types.x_ray_error_percent.XRayErrorPercent"
    ]
    """<p> The X-Ray request error percentage for this node. </p>"""
    x_ray_request_count: NotRequired[
        "aws_sdk_application_insights.types.x_ray_request_count.XRayRequestCount"
    ]
    """<p> The X-Ray request count for this node. </p>"""
    x_ray_request_average_latency: NotRequired[
        "aws_sdk_application_insights.types.x_ray_request_average_latency.XRayRequestAverageLatency"
    ]
    """<p> The X-Ray node request average latency for this node. </p>"""
    x_ray_node_name: NotRequired[
        "aws_sdk_application_insights.types.x_ray_node_name.XRayNodeName"
    ]
    """<p> The name of the X-Ray node. </p>"""
    x_ray_node_type: NotRequired[
        "aws_sdk_application_insights.types.x_ray_node_type.XRayNodeType"
    ]
    """<p> The type of the X-Ray node. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Observation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "start_time" in value:
        import aws_sdk_application_insights.types.start_time

        out["StartTime"] = (
            aws_sdk_application_insights.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_application_insights.types.end_time

        out["EndTime"] = (
            aws_sdk_application_insights.types.end_time.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "source_arn" in value:
        out["SourceARN"] = value["source_arn"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "line_time" in value:
        import aws_sdk_application_insights.types.line_time

        out["LineTime"] = (
            aws_sdk_application_insights.types.line_time.serialize_aws_json_1_1(
                value["line_time"]
            )
        )
    if "log_text" in value:
        out["LogText"] = value["log_text"]
    if "log_filter" in value:
        import aws_sdk_application_insights.types.log_filter

        out["LogFilter"] = (
            aws_sdk_application_insights.types.log_filter.serialize_aws_json_1_1(
                value["log_filter"]
            )
        )
    if "metric_namespace" in value:
        out["MetricNamespace"] = value["metric_namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "value" in value:
        out["Value"] = value["value"]
    if "cloud_watch_event_id" in value:
        out["CloudWatchEventId"] = value["cloud_watch_event_id"]
    if "cloud_watch_event_source" in value:
        import aws_sdk_application_insights.types.cloud_watch_event_source

        out["CloudWatchEventSource"] = (
            aws_sdk_application_insights.types.cloud_watch_event_source.serialize_aws_json_1_1(
                value["cloud_watch_event_source"]
            )
        )
    if "cloud_watch_event_detail_type" in value:
        out["CloudWatchEventDetailType"] = value["cloud_watch_event_detail_type"]
    if "health_event_arn" in value:
        out["HealthEventArn"] = value["health_event_arn"]
    if "health_service" in value:
        out["HealthService"] = value["health_service"]
    if "health_event_type_code" in value:
        out["HealthEventTypeCode"] = value["health_event_type_code"]
    if "health_event_type_category" in value:
        out["HealthEventTypeCategory"] = value["health_event_type_category"]
    if "health_event_description" in value:
        out["HealthEventDescription"] = value["health_event_description"]
    if "code_deploy_deployment_id" in value:
        out["CodeDeployDeploymentId"] = value["code_deploy_deployment_id"]
    if "code_deploy_deployment_group" in value:
        out["CodeDeployDeploymentGroup"] = value["code_deploy_deployment_group"]
    if "code_deploy_state" in value:
        out["CodeDeployState"] = value["code_deploy_state"]
    if "code_deploy_application" in value:
        out["CodeDeployApplication"] = value["code_deploy_application"]
    if "code_deploy_instance_group_id" in value:
        out["CodeDeployInstanceGroupId"] = value["code_deploy_instance_group_id"]
    if "ec2_state" in value:
        out["Ec2State"] = value["ec2_state"]
    if "rds_event_categories" in value:
        out["RdsEventCategories"] = value["rds_event_categories"]
    if "rds_event_message" in value:
        out["RdsEventMessage"] = value["rds_event_message"]
    if "s3_event_name" in value:
        out["S3EventName"] = value["s3_event_name"]
    if "states_execution_arn" in value:
        out["StatesExecutionArn"] = value["states_execution_arn"]
    if "states_arn" in value:
        out["StatesArn"] = value["states_arn"]
    if "states_status" in value:
        out["StatesStatus"] = value["states_status"]
    if "states_input" in value:
        out["StatesInput"] = value["states_input"]
    if "ebs_event" in value:
        out["EbsEvent"] = value["ebs_event"]
    if "ebs_result" in value:
        out["EbsResult"] = value["ebs_result"]
    if "ebs_cause" in value:
        out["EbsCause"] = value["ebs_cause"]
    if "ebs_request_id" in value:
        out["EbsRequestId"] = value["ebs_request_id"]
    if "x_ray_fault_percent" in value:
        out["XRayFaultPercent"] = value["x_ray_fault_percent"]
    if "x_ray_throttle_percent" in value:
        out["XRayThrottlePercent"] = value["x_ray_throttle_percent"]
    if "x_ray_error_percent" in value:
        out["XRayErrorPercent"] = value["x_ray_error_percent"]
    if "x_ray_request_count" in value:
        out["XRayRequestCount"] = value["x_ray_request_count"]
    if "x_ray_request_average_latency" in value:
        out["XRayRequestAverageLatency"] = value["x_ray_request_average_latency"]
    if "x_ray_node_name" in value:
        out["XRayNodeName"] = value["x_ray_node_name"]
    if "x_ray_node_type" in value:
        out["XRayNodeType"] = value["x_ray_node_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Observation:
    out: Observation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "StartTime" in data:
        import aws_sdk_application_insights.types.start_time

        out["start_time"] = (
            aws_sdk_application_insights.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_application_insights.types.end_time

        out["end_time"] = (
            aws_sdk_application_insights.types.end_time.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "SourceARN" in data:
        out["source_arn"] = data["SourceARN"]
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    if "LineTime" in data:
        import aws_sdk_application_insights.types.line_time

        out["line_time"] = (
            aws_sdk_application_insights.types.line_time.deserialize_aws_json_1_1(
                data["LineTime"]
            )
        )
    if "LogText" in data:
        out["log_text"] = data["LogText"]
    if "LogFilter" in data:
        import aws_sdk_application_insights.types.log_filter

        out["log_filter"] = (
            aws_sdk_application_insights.types.log_filter.deserialize_aws_json_1_1(
                data["LogFilter"]
            )
        )
    if "MetricNamespace" in data:
        out["metric_namespace"] = data["MetricNamespace"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "CloudWatchEventId" in data:
        out["cloud_watch_event_id"] = data["CloudWatchEventId"]
    if "CloudWatchEventSource" in data:
        import aws_sdk_application_insights.types.cloud_watch_event_source

        out["cloud_watch_event_source"] = (
            aws_sdk_application_insights.types.cloud_watch_event_source.deserialize_aws_json_1_1(
                data["CloudWatchEventSource"]
            )
        )
    if "CloudWatchEventDetailType" in data:
        out["cloud_watch_event_detail_type"] = data["CloudWatchEventDetailType"]
    if "HealthEventArn" in data:
        out["health_event_arn"] = data["HealthEventArn"]
    if "HealthService" in data:
        out["health_service"] = data["HealthService"]
    if "HealthEventTypeCode" in data:
        out["health_event_type_code"] = data["HealthEventTypeCode"]
    if "HealthEventTypeCategory" in data:
        out["health_event_type_category"] = data["HealthEventTypeCategory"]
    if "HealthEventDescription" in data:
        out["health_event_description"] = data["HealthEventDescription"]
    if "CodeDeployDeploymentId" in data:
        out["code_deploy_deployment_id"] = data["CodeDeployDeploymentId"]
    if "CodeDeployDeploymentGroup" in data:
        out["code_deploy_deployment_group"] = data["CodeDeployDeploymentGroup"]
    if "CodeDeployState" in data:
        out["code_deploy_state"] = data["CodeDeployState"]
    if "CodeDeployApplication" in data:
        out["code_deploy_application"] = data["CodeDeployApplication"]
    if "CodeDeployInstanceGroupId" in data:
        out["code_deploy_instance_group_id"] = data["CodeDeployInstanceGroupId"]
    if "Ec2State" in data:
        out["ec2_state"] = data["Ec2State"]
    if "RdsEventCategories" in data:
        out["rds_event_categories"] = data["RdsEventCategories"]
    if "RdsEventMessage" in data:
        out["rds_event_message"] = data["RdsEventMessage"]
    if "S3EventName" in data:
        out["s3_event_name"] = data["S3EventName"]
    if "StatesExecutionArn" in data:
        out["states_execution_arn"] = data["StatesExecutionArn"]
    if "StatesArn" in data:
        out["states_arn"] = data["StatesArn"]
    if "StatesStatus" in data:
        out["states_status"] = data["StatesStatus"]
    if "StatesInput" in data:
        out["states_input"] = data["StatesInput"]
    if "EbsEvent" in data:
        out["ebs_event"] = data["EbsEvent"]
    if "EbsResult" in data:
        out["ebs_result"] = data["EbsResult"]
    if "EbsCause" in data:
        out["ebs_cause"] = data["EbsCause"]
    if "EbsRequestId" in data:
        out["ebs_request_id"] = data["EbsRequestId"]
    if "XRayFaultPercent" in data:
        out["x_ray_fault_percent"] = data["XRayFaultPercent"]
    if "XRayThrottlePercent" in data:
        out["x_ray_throttle_percent"] = data["XRayThrottlePercent"]
    if "XRayErrorPercent" in data:
        out["x_ray_error_percent"] = data["XRayErrorPercent"]
    if "XRayRequestCount" in data:
        out["x_ray_request_count"] = data["XRayRequestCount"]
    if "XRayRequestAverageLatency" in data:
        out["x_ray_request_average_latency"] = data["XRayRequestAverageLatency"]
    if "XRayNodeName" in data:
        out["x_ray_node_name"] = data["XRayNodeName"]
    if "XRayNodeType" in data:
        out["x_ray_node_type"] = data["XRayNodeType"]
    return out
