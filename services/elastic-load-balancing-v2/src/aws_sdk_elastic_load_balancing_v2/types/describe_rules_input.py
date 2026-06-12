"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeRulesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.listener_arn
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.page_size
    import aws_sdk_elastic_load_balancing_v2.types.rule_arns


class DescribeRulesInput(TypedDict):
    listener_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    rule_arns: NotRequired["aws_sdk_elastic_load_balancing_v2.types.rule_arns.RuleArns"]
    """<p>The Amazon Resource Names (ARN) of the rules.</p>"""
    marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["aws_sdk_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listener_arn" in value:
        pairs.append((f"{prefix}.ListenerArn", str(value["listener_arn"])))
    if "rule_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rule_arns

        aws_sdk_elastic_load_balancing_v2.types.rule_arns.serialize_query(
            value["rule_arns"], pairs, f"{prefix}.RuleArns"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeRulesInput:
    out: DescribeRulesInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_rule_arns = el.find("RuleArns")
    if child_rule_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rule_arns

        out["rule_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.rule_arns.deserialize_query(
                child_rule_arns
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
