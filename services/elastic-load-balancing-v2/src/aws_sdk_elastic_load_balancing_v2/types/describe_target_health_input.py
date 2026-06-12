"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetHealthInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options
    import aws_sdk_elastic_load_balancing_v2.types.target_descriptions
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn


class DescribeTargetHealthInput(TypedDict):
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    targets: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_descriptions.TargetDescriptions"
    ]
    """<p>The targets.</p>"""
    include: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options.ListOfDescribeTargetHealthIncludeOptions"
    ]
    """<p>Used to include anomaly detection information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTargetHealthInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "targets" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_descriptions

        aws_sdk_elastic_load_balancing_v2.types.target_descriptions.serialize_query(
            value["targets"], pairs, f"{prefix}.Targets"
        )
    if "include" in value:
        import aws_sdk_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options

        aws_sdk_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options.serialize_query(
            value["include"], pairs, f"{prefix}.Include"
        )


def deserialize_query(el: Element) -> DescribeTargetHealthInput:
    out: DescribeTargetHealthInput = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_targets = el.find("Targets")
    if child_targets is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_descriptions

        out["targets"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_descriptions.deserialize_query(
                child_targets
            )
        )
    child_include = el.find("Include")
    if child_include is not None:
        import aws_sdk_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options

        out["include"] = (
            aws_sdk_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options.deserialize_query(
                child_include
            )
        )
    return out
