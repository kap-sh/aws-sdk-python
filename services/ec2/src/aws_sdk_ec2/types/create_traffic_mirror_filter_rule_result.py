"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter_rule


class CreateTrafficMirrorFilterRuleResult(TypedDict, closed=True):
    traffic_mirror_filter_rule: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule.TrafficMirrorFilterRule"
    ]
    """<p>The Traffic Mirror rule.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTrafficMirrorFilterRuleResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_filter_rule" in value:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule

        aws_sdk_ec2.types.traffic_mirror_filter_rule.serialize_ec2_query(
            value["traffic_mirror_filter_rule"],
            pairs,
            f"{prefix}.TrafficMirrorFilterRule",
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateTrafficMirrorFilterRuleResult:
    out: CreateTrafficMirrorFilterRuleResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule = el.find("TrafficMirrorFilterRule")
    if child_traffic_mirror_filter_rule is not None:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule

        out["traffic_mirror_filter_rule"] = (
            aws_sdk_ec2.types.traffic_mirror_filter_rule.deserialize_ec2_query(
                child_traffic_mirror_filter_rule
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
