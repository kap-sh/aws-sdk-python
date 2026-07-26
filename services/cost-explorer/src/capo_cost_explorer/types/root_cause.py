"""Generated from Smithy shape ``com.amazonaws.costexplorer#RootCause``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.root_cause_impact


class RootCause(TypedDict, closed=True):
    service: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services service name that's associated with the cost anomaly. </p>"""
    region: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region that's associated with the cost anomaly. </p>"""
    linked_account: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The member account value that's associated with the cost anomaly. </p>"""
    linked_account_name: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The member account name value that's associated with the cost anomaly.</p>"""
    usage_type: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The <code>UsageType</code> value that's associated with the cost anomaly. </p>"""
    impact: NotRequired["capo_cost_explorer.types.root_cause_impact.RootCauseImpact"]
    """<p>The dollar impact for the root cause.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RootCause) -> dict:
    out: dict = {}
    if "service" in value:
        out["Service"] = value["service"]
    if "region" in value:
        out["Region"] = value["region"]
    if "linked_account" in value:
        out["LinkedAccount"] = value["linked_account"]
    if "linked_account_name" in value:
        out["LinkedAccountName"] = value["linked_account_name"]
    if "usage_type" in value:
        out["UsageType"] = value["usage_type"]
    if "impact" in value:
        import capo_cost_explorer.types.root_cause_impact

        out["Impact"] = (
            capo_cost_explorer.types.root_cause_impact.serialize_aws_json_1_1(
                value["impact"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RootCause:
    out: RootCause = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        out["service"] = data["Service"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "LinkedAccount" in data:
        out["linked_account"] = data["LinkedAccount"]
    if "LinkedAccountName" in data:
        out["linked_account_name"] = data["LinkedAccountName"]
    if "UsageType" in data:
        out["usage_type"] = data["UsageType"]
    if "Impact" in data:
        import capo_cost_explorer.types.root_cause_impact

        out["impact"] = (
            capo_cost_explorer.types.root_cause_impact.deserialize_aws_json_1_1(
                data["Impact"]
            )
        )
    return out
