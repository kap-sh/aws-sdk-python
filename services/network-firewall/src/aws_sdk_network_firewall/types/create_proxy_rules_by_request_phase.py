"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRulesByRequestPhase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.create_proxy_rule_list


class CreateProxyRulesByRequestPhase(TypedDict):
    pre_dns: NotRequired[
        "aws_sdk_network_firewall.types.create_proxy_rule_list.CreateProxyRuleList"
    ]
    """<p>Before domain resolution. </p>"""
    pre_request: NotRequired[
        "aws_sdk_network_firewall.types.create_proxy_rule_list.CreateProxyRuleList"
    ]
    """<p>After DNS, before request.</p>"""
    post_response: NotRequired[
        "aws_sdk_network_firewall.types.create_proxy_rule_list.CreateProxyRuleList"
    ]
    """<p>After receiving response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRulesByRequestPhase) -> dict:
    out: dict = {}
    if "pre_dns" in value:
        import aws_sdk_network_firewall.types.create_proxy_rule_list

        out["PreDNS"] = (
            aws_sdk_network_firewall.types.create_proxy_rule_list.serialize_aws_json_1_0(
                value["pre_dns"]
            )
        )
    if "pre_request" in value:
        import aws_sdk_network_firewall.types.create_proxy_rule_list

        out["PreREQUEST"] = (
            aws_sdk_network_firewall.types.create_proxy_rule_list.serialize_aws_json_1_0(
                value["pre_request"]
            )
        )
    if "post_response" in value:
        import aws_sdk_network_firewall.types.create_proxy_rule_list

        out["PostRESPONSE"] = (
            aws_sdk_network_firewall.types.create_proxy_rule_list.serialize_aws_json_1_0(
                value["post_response"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyRulesByRequestPhase:
    out: CreateProxyRulesByRequestPhase = {}  # type: ignore[typeddict-item]
    if "PreDNS" in data:
        import aws_sdk_network_firewall.types.create_proxy_rule_list

        out["pre_dns"] = (
            aws_sdk_network_firewall.types.create_proxy_rule_list.deserialize_aws_json_1_0(
                data["PreDNS"]
            )
        )
    if "PreREQUEST" in data:
        import aws_sdk_network_firewall.types.create_proxy_rule_list

        out["pre_request"] = (
            aws_sdk_network_firewall.types.create_proxy_rule_list.deserialize_aws_json_1_0(
                data["PreREQUEST"]
            )
        )
    if "PostRESPONSE" in data:
        import aws_sdk_network_firewall.types.create_proxy_rule_list

        out["post_response"] = (
            aws_sdk_network_firewall.types.create_proxy_rule_list.deserialize_aws_json_1_0(
                data["PostRESPONSE"]
            )
        )
    return out
