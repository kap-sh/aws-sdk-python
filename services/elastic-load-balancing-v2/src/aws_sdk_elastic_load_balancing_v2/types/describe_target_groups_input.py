"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.page_size
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arns
    import aws_sdk_elastic_load_balancing_v2.types.target_group_names


class DescribeTargetGroupsInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    target_group_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arns.TargetGroupArns"
    ]
    """<p>The Amazon Resource Names (ARN) of the target groups.</p>"""
    names: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_names.TargetGroupNames"
    ]
    """<p>The names of the target groups.</p>"""
    marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["aws_sdk_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTargetGroupsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "target_group_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_arns

        aws_sdk_elastic_load_balancing_v2.types.target_group_arns.serialize_query(
            value["target_group_arns"], pairs, f"{prefix}.TargetGroupArns"
        )
    if "names" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_names

        aws_sdk_elastic_load_balancing_v2.types.target_group_names.serialize_query(
            value["names"], pairs, f"{prefix}.Names"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeTargetGroupsInput:
    out: DescribeTargetGroupsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_target_group_arns = el.find("TargetGroupArns")
    if child_target_group_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_arns

        out["target_group_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_group_arns.deserialize_query(
                child_target_group_arns
            )
        )
    child_names = el.find("Names")
    if child_names is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_names

        out["names"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_group_names.deserialize_query(
                child_names
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
