"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SummaryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.summary_rule_options


class SummaryConfiguration(TypedDict):
    rule_options: NotRequired[
        "aws_sdk_network_firewall.types.summary_rule_options.SummaryRuleOptions"
    ]
    """<p>Specifies the selected rule options returned by <a>DescribeRuleGroupSummary</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryConfiguration) -> dict:
    out: dict = {}
    if "rule_options" in value:
        import aws_sdk_network_firewall.types.summary_rule_options

        out["RuleOptions"] = (
            aws_sdk_network_firewall.types.summary_rule_options.serialize_aws_json_1_0(
                value["rule_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SummaryConfiguration:
    out: SummaryConfiguration = {}  # type: ignore[typeddict-item]
    if "RuleOptions" in data:
        import aws_sdk_network_firewall.types.summary_rule_options

        out["rule_options"] = (
            aws_sdk_network_firewall.types.summary_rule_options.deserialize_aws_json_1_0(
                data["RuleOptions"]
            )
        )
    return out
