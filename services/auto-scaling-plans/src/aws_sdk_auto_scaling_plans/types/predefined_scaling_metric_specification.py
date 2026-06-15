"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#PredefinedScalingMetricSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.resource_label
    import aws_sdk_auto_scaling_plans.types.scaling_metric_type


class PredefinedScalingMetricSpecification(TypedDict):
    predefined_scaling_metric_type: (
        "aws_sdk_auto_scaling_plans.types.scaling_metric_type.ScalingMetricType"
    )
    """<p>The metric type. The <code>ALBRequestCountPerTarget</code> metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.</p>"""
    resource_label: NotRequired[
        "aws_sdk_auto_scaling_plans.types.resource_label.ResourceLabel"
    ]
    r"""<p>Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is <code>ALBRequestCountPerTarget</code> and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service.</p> <p>You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:</p> <ul> <li> <p>app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN</p> </li> <li> <p>targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.</p> </li> </ul> <p>This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d.</p> <p>To find the ARN for an Application Load Balancer, use the <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html\">DescribeLoadBalancers</a> API operation. To find the ARN for the target group, use the <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html\">DescribeTargetGroups</a> API operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredefinedScalingMetricSpecification) -> dict:
    out: dict = {}
    import aws_sdk_auto_scaling_plans.types.scaling_metric_type

    out["PredefinedScalingMetricType"] = (
        aws_sdk_auto_scaling_plans.types.scaling_metric_type.serialize_aws_json_1_1(
            value["predefined_scaling_metric_type"]
        )
    )
    if "resource_label" in value:
        out["ResourceLabel"] = value["resource_label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredefinedScalingMetricSpecification:
    out: PredefinedScalingMetricSpecification = {}  # type: ignore[typeddict-item]
    if "PredefinedScalingMetricType" in data:
        import aws_sdk_auto_scaling_plans.types.scaling_metric_type

        out["predefined_scaling_metric_type"] = (
            aws_sdk_auto_scaling_plans.types.scaling_metric_type.deserialize_aws_json_1_1(
                data["PredefinedScalingMetricType"]
            )
        )
    else:
        raise DeserializationError(
            "PredefinedScalingMetricSpecification.predefined_scaling_metric_type required"
        )
    if "ResourceLabel" in data:
        out["resource_label"] = data["ResourceLabel"]
    return out
