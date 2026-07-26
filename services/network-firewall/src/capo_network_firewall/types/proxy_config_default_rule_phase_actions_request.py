"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyConfigDefaultRulePhaseActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_phase_action


class ProxyConfigDefaultRulePhaseActionsRequest(TypedDict, closed=True):
    pre_dns: NotRequired[
        "capo_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>Before domain resolution. </p>"""
    pre_request: NotRequired[
        "capo_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>After DNS, before request.</p>"""
    post_response: NotRequired[
        "capo_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>After receiving response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyConfigDefaultRulePhaseActionsRequest) -> dict:
    out: dict = {}
    if "pre_dns" in value:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["PreDNS"] = (
            capo_network_firewall.types.proxy_rule_phase_action.serialize_aws_json_1_0(
                value["pre_dns"]
            )
        )
    if "pre_request" in value:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["PreREQUEST"] = (
            capo_network_firewall.types.proxy_rule_phase_action.serialize_aws_json_1_0(
                value["pre_request"]
            )
        )
    if "post_response" in value:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["PostRESPONSE"] = (
            capo_network_firewall.types.proxy_rule_phase_action.serialize_aws_json_1_0(
                value["post_response"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyConfigDefaultRulePhaseActionsRequest:
    out: ProxyConfigDefaultRulePhaseActionsRequest = {}  # type: ignore[typeddict-item]
    if "PreDNS" in data:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["pre_dns"] = (
            capo_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["PreDNS"]
            )
        )
    if "PreREQUEST" in data:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["pre_request"] = (
            capo_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["PreREQUEST"]
            )
        )
    if "PostRESPONSE" in data:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["post_response"] = (
            capo_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["PostRESPONSE"]
            )
        )
    return out
