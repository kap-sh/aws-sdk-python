"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_configuration
    import aws_sdk_compute_optimizer.types.auto_scaling_group_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.gpu_info
    import aws_sdk_compute_optimizer.types.migration_effort
    import aws_sdk_compute_optimizer.types.performance_risk
    import aws_sdk_compute_optimizer.types.projected_utilization_metrics
    import aws_sdk_compute_optimizer.types.rank
    import aws_sdk_compute_optimizer.types.savings_opportunity


class AutoScalingGroupRecommendationOption(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_compute_optimizer.types.auto_scaling_group_configuration.AutoScalingGroupConfiguration"
    ]
    """<p>An array of objects that describe an Auto Scaling group configuration.</p>"""
    instance_gpu_info: NotRequired["aws_sdk_compute_optimizer.types.gpu_info.GpuInfo"]
    """<p> Describes the GPU accelerator settings for the recommended instance type of the Auto Scaling group. </p>"""
    projected_utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.projected_utilization_metrics.ProjectedUtilizationMetrics"
    ]
    r"""<p>An array of objects that describe the projected utilization metrics of the Auto Scaling group recommendation option.</p> <note> <p>The <code>Cpu</code> and <code>Memory</code> metrics are the only projected utilization metrics returned. Additionally, the <code>Memory</code> metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see <a href=\"https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent\">Enabling Memory Utilization with the CloudWatch Agent</a>.</p> </note>"""
    performance_risk: "aws_sdk_compute_optimizer.types.performance_risk.PerformanceRisk"
    """<p>The performance risk of the Auto Scaling group configuration recommendation.</p> <p>Performance risk indicates the likelihood of the recommended instance type not meeting the resource needs of your workload. Compute Optimizer calculates an individual performance risk score for each specification of the recommended instance, including CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.</p> <p>The value ranges from <code>0</code> - <code>4</code>, with <code>0</code> meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.</p>"""
    rank: "aws_sdk_compute_optimizer.types.rank.Rank"
    """<p>The rank of the Auto Scaling group recommendation option.</p> <p>The top recommendation option is ranked as <code>1</code>.</p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    """<p>An object that describes the savings opportunity for the Auto Scaling group recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.auto_scaling_group_savings_opportunity_after_discounts.AutoScalingGroupSavingsOpportunityAfterDiscounts"
    ]
    """<p> An object that describes the savings opportunity for the Auto Scaling group recommendation option that includes Savings Plans and Reserved Instances discounts. Savings opportunity includes the estimated monthly savings and percentage. </p>"""
    migration_effort: NotRequired[
        "aws_sdk_compute_optimizer.types.migration_effort.MigrationEffort"
    ]
    """<p>The level of effort required to migrate from the current instance type to the recommended instance type.</p> <p>For example, the migration effort is <code>Low</code> if Amazon EMR is the inferred workload type and an Amazon Web Services Graviton instance type is recommended. The migration effort is <code>Medium</code> if a workload type couldn't be inferred but an Amazon Web Services Graviton instance type is recommended. The migration effort is <code>VeryLow</code> if both the current and recommended instance types are of the same CPU architecture.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupRecommendationOption) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_compute_optimizer.types.auto_scaling_group_configuration

        out["configuration"] = (
            aws_sdk_compute_optimizer.types.auto_scaling_group_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "instance_gpu_info" in value:
        import aws_sdk_compute_optimizer.types.gpu_info

        out["instanceGpuInfo"] = (
            aws_sdk_compute_optimizer.types.gpu_info.serialize_aws_json_1_0(
                value["instance_gpu_info"]
            )
        )
    if "projected_utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.projected_utilization_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    out["performanceRisk"] = value.get("performance_risk", 0)
    out["rank"] = value.get("rank", 0)
    if "savings_opportunity" in value:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import aws_sdk_compute_optimizer.types.auto_scaling_group_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.auto_scaling_group_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "migration_effort" in value:
        import aws_sdk_compute_optimizer.types.migration_effort

        out["migrationEffort"] = (
            aws_sdk_compute_optimizer.types.migration_effort.serialize_aws_json_1_0(
                value["migration_effort"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingGroupRecommendationOption:
    out: AutoScalingGroupRecommendationOption = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_compute_optimizer.types.auto_scaling_group_configuration

        out["configuration"] = (
            aws_sdk_compute_optimizer.types.auto_scaling_group_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "instanceGpuInfo" in data:
        import aws_sdk_compute_optimizer.types.gpu_info

        out["instance_gpu_info"] = (
            aws_sdk_compute_optimizer.types.gpu_info.deserialize_aws_json_1_0(
                data["instanceGpuInfo"]
            )
        )
    if "projectedUtilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.projected_utilization_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if "performanceRisk" in data:
        out["performance_risk"] = data["performanceRisk"]
    else:
        out["performance_risk"] = 0
    if "rank" in data:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if "savingsOpportunity" in data:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if "savingsOpportunityAfterDiscounts" in data:
        import aws_sdk_compute_optimizer.types.auto_scaling_group_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.auto_scaling_group_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if "migrationEffort" in data:
        import aws_sdk_compute_optimizer.types.migration_effort

        out["migration_effort"] = (
            aws_sdk_compute_optimizer.types.migration_effort.deserialize_aws_json_1_0(
                data["migrationEffort"]
            )
        )
    return out
