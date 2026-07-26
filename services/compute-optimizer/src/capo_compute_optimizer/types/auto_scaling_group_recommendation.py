"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.auto_scaling_group_arn
    import capo_compute_optimizer.types.auto_scaling_group_configuration
    import capo_compute_optimizer.types.auto_scaling_group_name
    import capo_compute_optimizer.types.auto_scaling_group_recommendation_options
    import capo_compute_optimizer.types.current_performance_risk
    import capo_compute_optimizer.types.effective_recommendation_preferences
    import capo_compute_optimizer.types.finding
    import capo_compute_optimizer.types.gpu_info
    import capo_compute_optimizer.types.inferred_workload_types
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.utilization_metrics


class AutoScalingGroupRecommendation(TypedDict, closed=True):
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the Auto Scaling group.</p>"""
    auto_scaling_group_arn: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_group_arn.AutoScalingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Auto Scaling group.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_group_name.AutoScalingGroupName"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    finding: NotRequired["capo_compute_optimizer.types.finding.Finding"]
    """<p>The finding classification of the Auto Scaling group.</p> <p>Findings for Auto Scaling groups include:</p> <ul> <li> <p> <b> <code>NotOptimized</code> </b>—An Auto Scaling group is considered not optimized when Compute Optimizer identifies a recommendation that can provide better performance for your workload.</p> </li> <li> <p> <b> <code>Optimized</code> </b>—An Auto Scaling group is considered optimized when Compute Optimizer determines that the group is correctly provisioned to run your workload based on the chosen instance type. For optimized resources, Compute Optimizer might recommend a new generation instance type.</p> </li> </ul>"""
    utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.utilization_metrics.UtilizationMetrics"
    ]
    """<p>An array of objects that describe the utilization metrics of the Auto Scaling group.</p>"""
    look_back_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p>The number of days for which utilization metrics were analyzed for the Auto Scaling group.</p>"""
    current_configuration: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_group_configuration.AutoScalingGroupConfiguration"
    ]
    """<p>An array of objects that describe the current configuration of the Auto Scaling group.</p>"""
    current_instance_gpu_info: NotRequired[
        "capo_compute_optimizer.types.gpu_info.GpuInfo"
    ]
    """<p> Describes the GPU accelerator settings for the current instance type of the Auto Scaling group. </p>"""
    recommendation_options: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_group_recommendation_options.AutoScalingGroupRecommendationOptions"
    ]
    """<p>An array of objects that describe the recommendation options for the Auto Scaling group.</p>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p>The timestamp of when the Auto Scaling group recommendation was last generated.</p>"""
    current_performance_risk: NotRequired[
        "capo_compute_optimizer.types.current_performance_risk.CurrentPerformanceRisk"
    ]
    """<p>The risk of the current Auto Scaling group not meeting the performance needs of its workloads. The higher the risk, the more likely the current Auto Scaling group configuration has insufficient capacity and cannot meet workload requirements.</p>"""
    effective_recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.effective_recommendation_preferences.EffectiveRecommendationPreferences"
    ]
    """<p>An object that describes the effective recommendation preferences for the Auto Scaling group.</p>"""
    inferred_workload_types: NotRequired[
        "capo_compute_optimizer.types.inferred_workload_types.InferredWorkloadTypes"
    ]
    """<p>The applications that might be running on the instances in the Auto Scaling group as inferred by Compute Optimizer.</p> <p>Compute Optimizer can infer if one of the following applications might be running on the instances:</p> <ul> <li> <p> <code>AmazonEmr</code> - Infers that Amazon EMR might be running on the instances.</p> </li> <li> <p> <code>ApacheCassandra</code> - Infers that Apache Cassandra might be running on the instances.</p> </li> <li> <p> <code>ApacheHadoop</code> - Infers that Apache Hadoop might be running on the instances.</p> </li> <li> <p> <code>Memcached</code> - Infers that Memcached might be running on the instances.</p> </li> <li> <p> <code>NGINX</code> - Infers that NGINX might be running on the instances.</p> </li> <li> <p> <code>PostgreSql</code> - Infers that PostgreSQL might be running on the instances.</p> </li> <li> <p> <code>Redis</code> - Infers that Redis might be running on the instances.</p> </li> <li> <p> <code>Kafka</code> - Infers that Kafka might be running on the instance.</p> </li> <li> <p> <code>SQLServer</code> - Infers that SQLServer might be running on the instance.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupRecommendation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "auto_scaling_group_arn" in value:
        out["autoScalingGroupArn"] = value["auto_scaling_group_arn"]
    if "auto_scaling_group_name" in value:
        out["autoScalingGroupName"] = value["auto_scaling_group_name"]
    if "finding" in value:
        import capo_compute_optimizer.types.finding

        out["finding"] = capo_compute_optimizer.types.finding.serialize_aws_json_1_0(
            value["finding"]
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    out["lookBackPeriodInDays"] = value.get("look_back_period_in_days", 0)
    if "current_configuration" in value:
        import capo_compute_optimizer.types.auto_scaling_group_configuration

        out["currentConfiguration"] = (
            capo_compute_optimizer.types.auto_scaling_group_configuration.serialize_aws_json_1_0(
                value["current_configuration"]
            )
        )
    if "current_instance_gpu_info" in value:
        import capo_compute_optimizer.types.gpu_info

        out["currentInstanceGpuInfo"] = (
            capo_compute_optimizer.types.gpu_info.serialize_aws_json_1_0(
                value["current_instance_gpu_info"]
            )
        )
    if "recommendation_options" in value:
        import capo_compute_optimizer.types.auto_scaling_group_recommendation_options

        out["recommendationOptions"] = (
            capo_compute_optimizer.types.auto_scaling_group_recommendation_options.serialize_aws_json_1_0(
                value["recommendation_options"]
            )
        )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "current_performance_risk" in value:
        import capo_compute_optimizer.types.current_performance_risk

        out["currentPerformanceRisk"] = (
            capo_compute_optimizer.types.current_performance_risk.serialize_aws_json_1_0(
                value["current_performance_risk"]
            )
        )
    if "effective_recommendation_preferences" in value:
        import capo_compute_optimizer.types.effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    if "inferred_workload_types" in value:
        import capo_compute_optimizer.types.inferred_workload_types

        out["inferredWorkloadTypes"] = (
            capo_compute_optimizer.types.inferred_workload_types.serialize_aws_json_1_0(
                value["inferred_workload_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingGroupRecommendation:
    out: AutoScalingGroupRecommendation = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "autoScalingGroupArn" in data:
        out["auto_scaling_group_arn"] = data["autoScalingGroupArn"]
    if "autoScalingGroupName" in data:
        out["auto_scaling_group_name"] = data["autoScalingGroupName"]
    if "finding" in data:
        import capo_compute_optimizer.types.finding

        out["finding"] = capo_compute_optimizer.types.finding.deserialize_aws_json_1_0(
            data["finding"]
        )
    if "utilizationMetrics" in data:
        import capo_compute_optimizer.types.utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if "lookBackPeriodInDays" in data:
        out["look_back_period_in_days"] = data["lookBackPeriodInDays"]
    else:
        out["look_back_period_in_days"] = 0
    if "currentConfiguration" in data:
        import capo_compute_optimizer.types.auto_scaling_group_configuration

        out["current_configuration"] = (
            capo_compute_optimizer.types.auto_scaling_group_configuration.deserialize_aws_json_1_0(
                data["currentConfiguration"]
            )
        )
    if "currentInstanceGpuInfo" in data:
        import capo_compute_optimizer.types.gpu_info

        out["current_instance_gpu_info"] = (
            capo_compute_optimizer.types.gpu_info.deserialize_aws_json_1_0(
                data["currentInstanceGpuInfo"]
            )
        )
    if "recommendationOptions" in data:
        import capo_compute_optimizer.types.auto_scaling_group_recommendation_options

        out["recommendation_options"] = (
            capo_compute_optimizer.types.auto_scaling_group_recommendation_options.deserialize_aws_json_1_0(
                data["recommendationOptions"]
            )
        )
    if "lastRefreshTimestamp" in data:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "currentPerformanceRisk" in data:
        import capo_compute_optimizer.types.current_performance_risk

        out["current_performance_risk"] = (
            capo_compute_optimizer.types.current_performance_risk.deserialize_aws_json_1_0(
                data["currentPerformanceRisk"]
            )
        )
    if "effectiveRecommendationPreferences" in data:
        import capo_compute_optimizer.types.effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.effective_recommendation_preferences.deserialize_aws_json_1_0(
                data["effectiveRecommendationPreferences"]
            )
        )
    if "inferredWorkloadTypes" in data:
        import capo_compute_optimizer.types.inferred_workload_types

        out["inferred_workload_types"] = (
            capo_compute_optimizer.types.inferred_workload_types.deserialize_aws_json_1_0(
                data["inferredWorkloadTypes"]
            )
        )
    return out
