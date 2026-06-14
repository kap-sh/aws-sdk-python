"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleSetVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.capacity_unit
    import aws_sdk_wafv2.types.resource_arn
    import aws_sdk_wafv2.types.time_window_day
    import aws_sdk_wafv2.types.timestamp


class ManagedRuleSetVersion(TypedDict):
    associated_rule_group_arn: NotRequired[
        "aws_sdk_wafv2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the vendor rule group that's used to define the published version of your managed rule group. </p>"""
    capacity: NotRequired["aws_sdk_wafv2.types.capacity_unit.CapacityUnit"]
    r"""<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html\">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    forecasted_lifetime: NotRequired[
        "aws_sdk_wafv2.types.time_window_day.TimeWindowDay"
    ]
    """<p>The amount of time you expect this version of your managed rule group to last, in days. </p>"""
    publish_timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    r"""<p>The time that you first published this version. </p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, \"2016-09-27T14:50Z\". </p>"""
    last_update_timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    r"""<p>The last time that you updated this version. </p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, \"2016-09-27T14:50Z\". </p>"""
    expiry_timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    r"""<p>The time that this version is set to expire.</p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, \"2016-09-27T14:50Z\". </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleSetVersion) -> dict:
    out: dict = {}
    if "associated_rule_group_arn" in value:
        out["AssociatedRuleGroupArn"] = value["associated_rule_group_arn"]
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "forecasted_lifetime" in value:
        out["ForecastedLifetime"] = value["forecasted_lifetime"]
    if "publish_timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["PublishTimestamp"] = aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["publish_timestamp"]
        )
    if "last_update_timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["LastUpdateTimestamp"] = (
            aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "expiry_timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["ExpiryTimestamp"] = aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["expiry_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleSetVersion:
    out: ManagedRuleSetVersion = {}  # type: ignore[typeddict-item]
    if "AssociatedRuleGroupArn" in data:
        out["associated_rule_group_arn"] = data["AssociatedRuleGroupArn"]
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    if "ForecastedLifetime" in data:
        out["forecasted_lifetime"] = data["ForecastedLifetime"]
    if "PublishTimestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["publish_timestamp"] = (
            aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["PublishTimestamp"]
            )
        )
    if "LastUpdateTimestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["last_update_timestamp"] = (
            aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if "ExpiryTimestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["expiry_timestamp"] = (
            aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["ExpiryTimestamp"]
            )
        )
    return out
