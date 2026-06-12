"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Summary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.rule_summaries


class Summary(TypedDict):
    rule_summaries: NotRequired[
        "aws_sdk_network_firewall.types.rule_summaries.RuleSummaries"
    ]
    """<p>An array of <a>RuleSummary</a> objects containing individual rule details that had been configured by the rulegroup's SummaryConfiguration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Summary) -> dict:
    out: dict = {}
    if "rule_summaries" in value:
        import aws_sdk_network_firewall.types.rule_summaries

        out["RuleSummaries"] = (
            aws_sdk_network_firewall.types.rule_summaries.serialize_aws_json_1_0(
                value["rule_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if "RuleSummaries" in data:
        import aws_sdk_network_firewall.types.rule_summaries

        out["rule_summaries"] = (
            aws_sdk_network_firewall.types.rule_summaries.deserialize_aws_json_1_0(
                data["RuleSummaries"]
            )
        )
    return out
