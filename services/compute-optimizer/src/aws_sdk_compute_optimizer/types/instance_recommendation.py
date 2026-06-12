"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_id
    import aws_sdk_compute_optimizer.types.current_instance_type
    import aws_sdk_compute_optimizer.types.current_performance_risk
    import aws_sdk_compute_optimizer.types.effective_recommendation_preferences
    import aws_sdk_compute_optimizer.types.external_metric_status
    import aws_sdk_compute_optimizer.types.finding
    import aws_sdk_compute_optimizer.types.gpu_info
    import aws_sdk_compute_optimizer.types.inferred_workload_types
    import aws_sdk_compute_optimizer.types.instance_arn
    import aws_sdk_compute_optimizer.types.instance_idle
    import aws_sdk_compute_optimizer.types.instance_name
    import aws_sdk_compute_optimizer.types.instance_recommendation_finding_reason_codes
    import aws_sdk_compute_optimizer.types.instance_state
    import aws_sdk_compute_optimizer.types.last_refresh_timestamp
    import aws_sdk_compute_optimizer.types.look_back_period_in_days
    import aws_sdk_compute_optimizer.types.recommendation_options
    import aws_sdk_compute_optimizer.types.recommendation_sources
    import aws_sdk_compute_optimizer.types.tags
    import aws_sdk_compute_optimizer.types.utilization_metrics


class InstanceRecommendation(TypedDict):
    instance_arn: NotRequired[
        "aws_sdk_compute_optimizer.types.instance_arn.InstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the current instance.</p>"""
    account_id: NotRequired["aws_sdk_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the instance.</p>"""
    instance_name: NotRequired[
        "aws_sdk_compute_optimizer.types.instance_name.InstanceName"
    ]
    """<p>The name of the current instance.</p>"""
    current_instance_type: NotRequired[
        "aws_sdk_compute_optimizer.types.current_instance_type.CurrentInstanceType"
    ]
    """<p>The instance type of the current instance.</p>"""
    finding: NotRequired["aws_sdk_compute_optimizer.types.finding.Finding"]
    """<p>The finding classification of the instance.</p> <p>Findings for instances include:</p> <ul> <li> <p> <b> <code>Underprovisioned</code> </b>—An instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned instances may lead to poor application performance.</p> </li> <li> <p> <b> <code>Overprovisioned</code> </b>—An instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and no specification is under-provisioned. Over-provisioned instances may lead to unnecessary infrastructure cost.</p> </li> <li> <p> <b> <code>Optimized</code> </b>—An instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload and is not over provisioned. For optimized resources, Compute Optimizer might recommend a new generation instance type.</p> </li> </ul> <note> <p>The valid values in your API responses appear as OVER_PROVISIONED, UNDER_PROVISIONED, or OPTIMIZED.</p> </note>"""
    finding_reason_codes: NotRequired[
        "aws_sdk_compute_optimizer.types.instance_recommendation_finding_reason_codes.InstanceRecommendationFindingReasonCodes"
    ]
    """<p>The reason for the finding classification of the instance.</p> <p>Finding reason codes for instances include:</p> <ul> <li> <p> <b> <code>CPUOverprovisioned</code> </b> — The instance’s CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>CPUUtilization</code> metric of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>CPUUnderprovisioned</code> </b> — The instance’s CPU configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance. This is identified by analyzing the <code>CPUUtilization</code> metric of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>MemoryOverprovisioned</code> </b> — The instance’s memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the memory utilization metric of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>MemoryUnderprovisioned</code> </b> — The instance’s memory configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance. This is identified by analyzing the memory utilization metric of the current instance during the look-back period.</p> <note> <p>Memory utilization is analyzed only for resources that have the unified CloudWatch agent installed on them. For more information, see <a href=\"https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent\">Enabling memory utilization with the Amazon CloudWatch Agent</a> in the <i>Compute Optimizer User Guide</i>. On Linux instances, Compute Optimizer analyses the <code>mem_used_percent</code> metric in the <code>CWAgent</code> namespace, or the legacy <code>MemoryUtilization</code> metric in the <code>System/Linux</code> namespace. On Windows instances, Compute Optimizer analyses the <code>Memory % Committed Bytes In Use</code> metric in the <code>CWAgent</code> namespace.</p> </note> </li> <li> <p> <b> <code>EBSThroughputOverprovisioned</code> </b> — The instance’s EBS throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>VolumeReadBytes</code> and <code>VolumeWriteBytes</code> metrics of EBS volumes attached to the current instance during the look-back period.</p> </li> <li> <p> <b> <code>EBSThroughputUnderprovisioned</code> </b> — The instance’s EBS throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the <code>VolumeReadBytes</code> and <code>VolumeWriteBytes</code> metrics of EBS volumes attached to the current instance during the look-back period.</p> </li> <li> <p> <b> <code>EBSIOPSOverprovisioned</code> </b> — The instance’s EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>VolumeReadOps</code> and <code>VolumeWriteOps</code> metric of EBS volumes attached to the current instance during the look-back period.</p> </li> <li> <p> <b> <code>EBSIOPSUnderprovisioned</code> </b> — The instance’s EBS IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance. This is identified by analyzing the <code>VolumeReadOps</code> and <code>VolumeWriteOps</code> metric of EBS volumes attached to the current instance during the look-back period.</p> </li> <li> <p> <b> <code>NetworkBandwidthOverprovisioned</code> </b> — The instance’s network bandwidth configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>NetworkIn</code> and <code>NetworkOut</code> metrics of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>NetworkBandwidthUnderprovisioned</code> </b> — The instance’s network bandwidth configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This is identified by analyzing the <code>NetworkIn</code> and <code>NetworkOut</code> metrics of the current instance during the look-back period. This finding reason happens when the <code>NetworkIn</code> or <code>NetworkOut</code> performance of an instance is impacted.</p> </li> <li> <p> <b> <code>NetworkPPSOverprovisioned</code> </b> — The instance’s network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>NetworkPacketsIn</code> and <code>NetworkPacketsIn</code> metrics of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>NetworkPPSUnderprovisioned</code> </b> — The instance’s network PPS (packets per second) configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance. This is identified by analyzing the <code>NetworkPacketsIn</code> and <code>NetworkPacketsIn</code> metrics of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>DiskIOPSOverprovisioned</code> </b> — The instance’s disk IOPS configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>DiskReadOps</code> and <code>DiskWriteOps</code> metrics of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>DiskIOPSUnderprovisioned</code> </b> — The instance’s disk IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance. This is identified by analyzing the <code>DiskReadOps</code> and <code>DiskWriteOps</code> metrics of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>DiskThroughputOverprovisioned</code> </b> — The instance’s disk throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>DiskReadBytes</code> and <code>DiskWriteBytes</code> metrics of the current instance during the look-back period.</p> </li> <li> <p> <b> <code>DiskThroughputUnderprovisioned</code> </b> — The instance’s disk throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance. This is identified by analyzing the <code>DiskReadBytes</code> and <code>DiskWriteBytes</code> metrics of the current instance during the look-back period.</p> </li> </ul> <note> <p>For more information about instance metrics, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html\">List the available CloudWatch metrics for your instances</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about EBS volume metrics, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html\">Amazon CloudWatch metrics for Amazon EBS</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>"""
    utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.utilization_metrics.UtilizationMetrics"
    ]
    """<p>An array of objects that describe the utilization metrics of the instance.</p>"""
    look_back_period_in_days: (
        "aws_sdk_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p>The number of days for which utilization metrics were analyzed for the instance.</p>"""
    recommendation_options: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_options.RecommendationOptions"
    ]
    """<p>An array of objects that describe the recommendation options for the instance.</p>"""
    recommendation_sources: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_sources.RecommendationSources"
    ]
    """<p>An array of objects that describe the source resource of the recommendation.</p>"""
    last_refresh_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p>The timestamp of when the instance recommendation was last generated.</p>"""
    current_performance_risk: NotRequired[
        "aws_sdk_compute_optimizer.types.current_performance_risk.CurrentPerformanceRisk"
    ]
    """<p>The risk of the current instance not meeting the performance needs of its workloads. The higher the risk, the more likely the current instance cannot meet the performance requirements of its workload.</p>"""
    effective_recommendation_preferences: NotRequired[
        "aws_sdk_compute_optimizer.types.effective_recommendation_preferences.EffectiveRecommendationPreferences"
    ]
    """<p>An object that describes the effective recommendation preferences for the instance.</p>"""
    inferred_workload_types: NotRequired[
        "aws_sdk_compute_optimizer.types.inferred_workload_types.InferredWorkloadTypes"
    ]
    """<p>The applications that might be running on the instance as inferred by Compute Optimizer.</p> <p>Compute Optimizer can infer if one of the following applications might be running on the instance:</p> <ul> <li> <p> <code>AmazonEmr</code> - Infers that Amazon EMR might be running on the instance.</p> </li> <li> <p> <code>ApacheCassandra</code> - Infers that Apache Cassandra might be running on the instance.</p> </li> <li> <p> <code>ApacheHadoop</code> - Infers that Apache Hadoop might be running on the instance.</p> </li> <li> <p> <code>Memcached</code> - Infers that Memcached might be running on the instance.</p> </li> <li> <p> <code>NGINX</code> - Infers that NGINX might be running on the instance.</p> </li> <li> <p> <code>PostgreSql</code> - Infers that PostgreSQL might be running on the instance.</p> </li> <li> <p> <code>Redis</code> - Infers that Redis might be running on the instance.</p> </li> <li> <p> <code>Kafka</code> - Infers that Kafka might be running on the instance.</p> </li> <li> <p> <code>SQLServer</code> - Infers that SQLServer might be running on the instance.</p> </li> </ul>"""
    instance_state: NotRequired[
        "aws_sdk_compute_optimizer.types.instance_state.InstanceState"
    ]
    """<p> The state of the instance when the recommendation was generated. </p>"""
    tags: NotRequired["aws_sdk_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to your Amazon EC2 instance recommendations. </p>"""
    external_metric_status: NotRequired[
        "aws_sdk_compute_optimizer.types.external_metric_status.ExternalMetricStatus"
    ]
    """<p> An object that describes Compute Optimizer's integration status with your external metrics provider. </p>"""
    current_instance_gpu_info: NotRequired[
        "aws_sdk_compute_optimizer.types.gpu_info.GpuInfo"
    ]
    """<p> Describes the GPU accelerator settings for the current instance type. </p>"""
    idle: NotRequired["aws_sdk_compute_optimizer.types.instance_idle.InstanceIdle"]
    """<p> Describes if an Amazon EC2 instance is idle. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceRecommendation) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "current_instance_type" in value:
        out["currentInstanceType"] = value["current_instance_type"]
    if "finding" in value:
        import aws_sdk_compute_optimizer.types.finding

        out["finding"] = aws_sdk_compute_optimizer.types.finding.serialize_aws_json_1_0(
            value["finding"]
        )
    if "finding_reason_codes" in value:
        import aws_sdk_compute_optimizer.types.instance_recommendation_finding_reason_codes

        out["findingReasonCodes"] = (
            aws_sdk_compute_optimizer.types.instance_recommendation_finding_reason_codes.serialize_aws_json_1_0(
                value["finding_reason_codes"]
            )
        )
    if "utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.utilization_metrics

        out["utilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    out["lookBackPeriodInDays"] = value.get("look_back_period_in_days", 0)
    if "recommendation_options" in value:
        import aws_sdk_compute_optimizer.types.recommendation_options

        out["recommendationOptions"] = (
            aws_sdk_compute_optimizer.types.recommendation_options.serialize_aws_json_1_0(
                value["recommendation_options"]
            )
        )
    if "recommendation_sources" in value:
        import aws_sdk_compute_optimizer.types.recommendation_sources

        out["recommendationSources"] = (
            aws_sdk_compute_optimizer.types.recommendation_sources.serialize_aws_json_1_0(
                value["recommendation_sources"]
            )
        )
    if "last_refresh_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "current_performance_risk" in value:
        import aws_sdk_compute_optimizer.types.current_performance_risk

        out["currentPerformanceRisk"] = (
            aws_sdk_compute_optimizer.types.current_performance_risk.serialize_aws_json_1_0(
                value["current_performance_risk"]
            )
        )
    if "effective_recommendation_preferences" in value:
        import aws_sdk_compute_optimizer.types.effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            aws_sdk_compute_optimizer.types.effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    if "inferred_workload_types" in value:
        import aws_sdk_compute_optimizer.types.inferred_workload_types

        out["inferredWorkloadTypes"] = (
            aws_sdk_compute_optimizer.types.inferred_workload_types.serialize_aws_json_1_0(
                value["inferred_workload_types"]
            )
        )
    if "instance_state" in value:
        import aws_sdk_compute_optimizer.types.instance_state

        out["instanceState"] = (
            aws_sdk_compute_optimizer.types.instance_state.serialize_aws_json_1_0(
                value["instance_state"]
            )
        )
    if "tags" in value:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "external_metric_status" in value:
        import aws_sdk_compute_optimizer.types.external_metric_status

        out["externalMetricStatus"] = (
            aws_sdk_compute_optimizer.types.external_metric_status.serialize_aws_json_1_0(
                value["external_metric_status"]
            )
        )
    if "current_instance_gpu_info" in value:
        import aws_sdk_compute_optimizer.types.gpu_info

        out["currentInstanceGpuInfo"] = (
            aws_sdk_compute_optimizer.types.gpu_info.serialize_aws_json_1_0(
                value["current_instance_gpu_info"]
            )
        )
    if "idle" in value:
        import aws_sdk_compute_optimizer.types.instance_idle

        out["idle"] = (
            aws_sdk_compute_optimizer.types.instance_idle.serialize_aws_json_1_0(
                value["idle"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceRecommendation:
    out: InstanceRecommendation = {}  # type: ignore[typeddict-item]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "currentInstanceType" in data:
        out["current_instance_type"] = data["currentInstanceType"]
    if "finding" in data:
        import aws_sdk_compute_optimizer.types.finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if "findingReasonCodes" in data:
        import aws_sdk_compute_optimizer.types.instance_recommendation_finding_reason_codes

        out["finding_reason_codes"] = (
            aws_sdk_compute_optimizer.types.instance_recommendation_finding_reason_codes.deserialize_aws_json_1_0(
                data["findingReasonCodes"]
            )
        )
    if "utilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.utilization_metrics

        out["utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if "lookBackPeriodInDays" in data:
        out["look_back_period_in_days"] = data["lookBackPeriodInDays"]
    else:
        out["look_back_period_in_days"] = 0
    if "recommendationOptions" in data:
        import aws_sdk_compute_optimizer.types.recommendation_options

        out["recommendation_options"] = (
            aws_sdk_compute_optimizer.types.recommendation_options.deserialize_aws_json_1_0(
                data["recommendationOptions"]
            )
        )
    if "recommendationSources" in data:
        import aws_sdk_compute_optimizer.types.recommendation_sources

        out["recommendation_sources"] = (
            aws_sdk_compute_optimizer.types.recommendation_sources.deserialize_aws_json_1_0(
                data["recommendationSources"]
            )
        )
    if "lastRefreshTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "currentPerformanceRisk" in data:
        import aws_sdk_compute_optimizer.types.current_performance_risk

        out["current_performance_risk"] = (
            aws_sdk_compute_optimizer.types.current_performance_risk.deserialize_aws_json_1_0(
                data["currentPerformanceRisk"]
            )
        )
    if "effectiveRecommendationPreferences" in data:
        import aws_sdk_compute_optimizer.types.effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            aws_sdk_compute_optimizer.types.effective_recommendation_preferences.deserialize_aws_json_1_0(
                data["effectiveRecommendationPreferences"]
            )
        )
    if "inferredWorkloadTypes" in data:
        import aws_sdk_compute_optimizer.types.inferred_workload_types

        out["inferred_workload_types"] = (
            aws_sdk_compute_optimizer.types.inferred_workload_types.deserialize_aws_json_1_0(
                data["inferredWorkloadTypes"]
            )
        )
    if "instanceState" in data:
        import aws_sdk_compute_optimizer.types.instance_state

        out["instance_state"] = (
            aws_sdk_compute_optimizer.types.instance_state.deserialize_aws_json_1_0(
                data["instanceState"]
            )
        )
    if "tags" in data:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "externalMetricStatus" in data:
        import aws_sdk_compute_optimizer.types.external_metric_status

        out["external_metric_status"] = (
            aws_sdk_compute_optimizer.types.external_metric_status.deserialize_aws_json_1_0(
                data["externalMetricStatus"]
            )
        )
    if "currentInstanceGpuInfo" in data:
        import aws_sdk_compute_optimizer.types.gpu_info

        out["current_instance_gpu_info"] = (
            aws_sdk_compute_optimizer.types.gpu_info.deserialize_aws_json_1_0(
                data["currentInstanceGpuInfo"]
            )
        )
    if "idle" in data:
        import aws_sdk_compute_optimizer.types.instance_idle

        out["idle"] = (
            aws_sdk_compute_optimizer.types.instance_idle.deserialize_aws_json_1_0(
                data["idle"]
            )
        )
    return out
