"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRulesByRequestPhase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.create_proxy_rule_list


class CreateProxyRulesByRequestPhase(TypedDict, closed=True):
    pre_dns: NotRequired[
        "capo_network_firewall.types.create_proxy_rule_list.CreateProxyRuleList"
    ]
    """<p>Before domain resolution. </p>"""
    pre_request: NotRequired[
        "capo_network_firewall.types.create_proxy_rule_list.CreateProxyRuleList"
    ]
    """<p>After DNS, before request.</p>"""
    post_response: NotRequired[
        "capo_network_firewall.types.create_proxy_rule_list.CreateProxyRuleList"
    ]
    """<p>After receiving response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRulesByRequestPhase) -> dict:
    out: dict = {}
    if "pre_dns" in value:
        import capo_network_firewall.types.create_proxy_rule_list

        out["PreDNS"] = (
            capo_network_firewall.types.create_proxy_rule_list.serialize_aws_json_1_0(
                value["pre_dns"]
            )
        )
    if "pre_request" in value:
        import capo_network_firewall.types.create_proxy_rule_list

        out["PreREQUEST"] = (
            capo_network_firewall.types.create_proxy_rule_list.serialize_aws_json_1_0(
                value["pre_request"]
            )
        )
    if "post_response" in value:
        import capo_network_firewall.types.create_proxy_rule_list

        out["PostRESPONSE"] = (
            capo_network_firewall.types.create_proxy_rule_list.serialize_aws_json_1_0(
                value["post_response"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyRulesByRequestPhase:
    out: CreateProxyRulesByRequestPhase = {}  # type: ignore[typeddict-item]
    if "PreDNS" in data:
        import capo_network_firewall.types.create_proxy_rule_list

        out["pre_dns"] = (
            capo_network_firewall.types.create_proxy_rule_list.deserialize_aws_json_1_0(
                data["PreDNS"]
            )
        )
    if "PreREQUEST" in data:
        import capo_network_firewall.types.create_proxy_rule_list

        out["pre_request"] = (
            capo_network_firewall.types.create_proxy_rule_list.deserialize_aws_json_1_0(
                data["PreREQUEST"]
            )
        )
    if "PostRESPONSE" in data:
        import capo_network_firewall.types.create_proxy_rule_list

        out["post_response"] = (
            capo_network_firewall.types.create_proxy_rule_list.deserialize_aws_json_1_0(
                data["PostRESPONSE"]
            )
        )
    return out
