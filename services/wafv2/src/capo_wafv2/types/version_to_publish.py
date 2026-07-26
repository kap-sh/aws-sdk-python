"""Generated from Smithy shape ``com.amazonaws.wafv2#VersionToPublish``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.time_window_day


class VersionToPublish(TypedDict, closed=True):
    associated_rule_group_arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the vendor's rule group that's used in the published managed rule group version. </p>"""
    forecasted_lifetime: NotRequired["capo_wafv2.types.time_window_day.TimeWindowDay"]
    """<p>The amount of time the vendor expects this version of the managed rule group to last, in days. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionToPublish) -> dict:
    out: dict = {}
    if "associated_rule_group_arn" in value:
        out["AssociatedRuleGroupArn"] = value["associated_rule_group_arn"]
    if "forecasted_lifetime" in value:
        out["ForecastedLifetime"] = value["forecasted_lifetime"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VersionToPublish:
    out: VersionToPublish = {}  # type: ignore[typeddict-item]
    if "AssociatedRuleGroupArn" in data:
        out["associated_rule_group_arn"] = data["AssociatedRuleGroupArn"]
    if "ForecastedLifetime" in data:
        out["forecasted_lifetime"] = data["ForecastedLifetime"]
    return out
