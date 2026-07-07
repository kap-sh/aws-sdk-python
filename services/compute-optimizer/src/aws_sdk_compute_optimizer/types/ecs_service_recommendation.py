"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_id
    import aws_sdk_compute_optimizer.types.current_performance_risk
    import aws_sdk_compute_optimizer.types.ecs_effective_recommendation_preferences
    import aws_sdk_compute_optimizer.types.ecs_service_launch_type
    import aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding
    import aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes
    import aws_sdk_compute_optimizer.types.ecs_service_recommendation_options
    import aws_sdk_compute_optimizer.types.ecs_service_utilization_metrics
    import aws_sdk_compute_optimizer.types.last_refresh_timestamp
    import aws_sdk_compute_optimizer.types.look_back_period_in_days
    import aws_sdk_compute_optimizer.types.service_arn
    import aws_sdk_compute_optimizer.types.service_configuration
    import aws_sdk_compute_optimizer.types.tags


class ECSServiceRecommendation(TypedDict, closed=True):
    service_arn: NotRequired["aws_sdk_compute_optimizer.types.service_arn.ServiceArn"]
    """<p> The Amazon Resource Name (ARN) of the current Amazon ECS service. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p>"""
    account_id: NotRequired["aws_sdk_compute_optimizer.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID of the Amazon ECS service. </p>"""
    current_service_configuration: NotRequired[
        "aws_sdk_compute_optimizer.types.service_configuration.ServiceConfiguration"
    ]
    """<p> The configuration of the current Amazon ECS service. </p>"""
    utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_utilization_metrics.ECSServiceUtilizationMetrics"
    ]
    """<p> An array of objects that describe the utilization metrics of the Amazon ECS service. </p>"""
    lookback_period_in_days: (
        "aws_sdk_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p> The number of days the Amazon ECS service utilization metrics were analyzed. </p>"""
    launch_type: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_launch_type.ECSServiceLaunchType"
    ]
    """<p> The launch type the Amazon ECS service is using. </p> <note> <p>Compute Optimizer only supports the Fargate launch type.</p> </note>"""
    last_refresh_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p> The timestamp of when the Amazon ECS service recommendation was last generated. </p>"""
    finding: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding.ECSServiceRecommendationFinding"
    ]
    """<p> The finding classification of an Amazon ECS service. </p> <p>Findings for Amazon ECS services include:</p> <ul> <li> <p> <b> <code>Underprovisioned</code> </b> — When Compute Optimizer detects that there’s not enough memory or CPU, an Amazon ECS service is considered under-provisioned. An under-provisioned service might result in poor application performance.</p> </li> <li> <p> <b> <code>Overprovisioned</code> </b> — When Compute Optimizer detects that there’s excessive memory or CPU, an Amazon ECS service is considered over-provisioned. An over-provisioned service might result in additional infrastructure costs. </p> </li> <li> <p> <b> <code>Optimized</code> </b> — When both the CPU and memory of your Amazon ECS service meet the performance requirements of your workload, the service is considered optimized.</p> </li> </ul>"""
    finding_reason_codes: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.ECSServiceRecommendationFindingReasonCodes"
    ]
    """<p> The reason for the finding classification of an Amazon ECS service. </p> <p>Finding reason codes for Amazon ECS services include:</p> <ul> <li> <p> <b> <code>CPUUnderprovisioned</code> </b> — The service CPU configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the <code>CPUUtilization</code> metric of the current service during the look-back period.</p> </li> <li> <p> <b> <code>CPUOverprovisioned</code> </b> — The service CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>CPUUtilization</code> metric of the current service during the look-back period. </p> </li> <li> <p> <b> <code>MemoryUnderprovisioned</code> </b> — The service memory configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the <code>MemoryUtilization</code> metric of the current service during the look-back period.</p> </li> <li> <p> <b> <code>MemoryOverprovisioned</code> </b> — The service memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>MemoryUtilization</code> metric of the current service during the look-back period.</p> </li> </ul>"""
    service_recommendation_options: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_recommendation_options.ECSServiceRecommendationOptions"
    ]
    """<p> An array of objects that describe the recommendation options for the Amazon ECS service. </p>"""
    current_performance_risk: NotRequired[
        "aws_sdk_compute_optimizer.types.current_performance_risk.CurrentPerformanceRisk"
    ]
    """<p> The risk of the current Amazon ECS service not meeting the performance needs of its workloads. The higher the risk, the more likely the current service can't meet the performance requirements of its workload. </p>"""
    effective_recommendation_preferences: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_effective_recommendation_preferences.ECSEffectiveRecommendationPreferences"
    ]
    """<p> Describes the effective recommendation preferences for Amazon ECS services. </p>"""
    tags: NotRequired["aws_sdk_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to your Amazon ECS service recommendations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendation) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_service_configuration" in value:
        import aws_sdk_compute_optimizer.types.service_configuration

        out["currentServiceConfiguration"] = (
            aws_sdk_compute_optimizer.types.service_configuration.serialize_aws_json_1_0(
                value["current_service_configuration"]
            )
        )
    if "utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_utilization_metrics

        out["utilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    out["lookbackPeriodInDays"] = value.get("lookback_period_in_days", 0)
    if "launch_type" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_launch_type

        out["launchType"] = (
            aws_sdk_compute_optimizer.types.ecs_service_launch_type.serialize_aws_json_1_0(
                value["launch_type"]
            )
        )
    if "last_refresh_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_reason_codes" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes

        out["findingReasonCodes"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.serialize_aws_json_1_0(
                value["finding_reason_codes"]
            )
        )
    if "service_recommendation_options" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_recommendation_options

        out["serviceRecommendationOptions"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_options.serialize_aws_json_1_0(
                value["service_recommendation_options"]
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
        import aws_sdk_compute_optimizer.types.ecs_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            aws_sdk_compute_optimizer.types.ecs_effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    if "tags" in value:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceRecommendation:
    out: ECSServiceRecommendation = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "currentServiceConfiguration" in data:
        import aws_sdk_compute_optimizer.types.service_configuration

        out["current_service_configuration"] = (
            aws_sdk_compute_optimizer.types.service_configuration.deserialize_aws_json_1_0(
                data["currentServiceConfiguration"]
            )
        )
    if "utilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_utilization_metrics

        out["utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if "lookbackPeriodInDays" in data:
        out["lookback_period_in_days"] = data["lookbackPeriodInDays"]
    else:
        out["lookback_period_in_days"] = 0
    if "launchType" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_launch_type

        out["launch_type"] = (
            aws_sdk_compute_optimizer.types.ecs_service_launch_type.deserialize_aws_json_1_0(
                data["launchType"]
            )
        )
    if "lastRefreshTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "finding" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if "findingReasonCodes" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes

        out["finding_reason_codes"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.deserialize_aws_json_1_0(
                data["findingReasonCodes"]
            )
        )
    if "serviceRecommendationOptions" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_recommendation_options

        out["service_recommendation_options"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_options.deserialize_aws_json_1_0(
                data["serviceRecommendationOptions"]
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
        import aws_sdk_compute_optimizer.types.ecs_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            aws_sdk_compute_optimizer.types.ecs_effective_recommendation_preferences.deserialize_aws_json_1_0(
                data["effectiveRecommendationPreferences"]
            )
        )
    if "tags" in data:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
