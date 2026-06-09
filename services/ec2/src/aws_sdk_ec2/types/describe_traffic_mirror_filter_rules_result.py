"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFilterRulesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_set


class DescribeTrafficMirrorFilterRulesResult(TypedDict):
    traffic_mirror_filter_rules: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_set.TrafficMirrorFilterRuleSet"
    ]
    """<p>Traffic mirror rules.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorFilterRulesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_filter_rules" in value:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule_set

        aws_sdk_ec2.types.traffic_mirror_filter_rule_set.serialize_ec2_query(
            value["traffic_mirror_filter_rules"],
            pairs,
            f"{prefix}.TrafficMirrorFilterRuleSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorFilterRulesResult:
    out: DescribeTrafficMirrorFilterRulesResult = {}  # type: ignore[typeddict-item]
    if el.find("TrafficMirrorFilterRuleSet") is not None:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule_set

        out["traffic_mirror_filter_rules"] = (
            aws_sdk_ec2.types.traffic_mirror_filter_rule_set.deserialize_ec2_query(
                el, "TrafficMirrorFilterRuleSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
