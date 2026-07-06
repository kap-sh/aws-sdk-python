"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.custom_header_list
    import aws_sdk_securityagent.types.network_traffic_rule_list


class NetworkTrafficConfig(TypedDict, closed=True):
    rules: NotRequired[
        "aws_sdk_securityagent.types.network_traffic_rule_list.NetworkTrafficRuleList"
    ]
    """<p>The list of network traffic rules that control which URLs are allowed or denied during testing.</p>"""
    custom_headers: NotRequired[
        "aws_sdk_securityagent.types.custom_header_list.CustomHeaderList"
    ]
    """<p>The list of custom HTTP headers to include in network traffic during testing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTrafficConfig) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_securityagent.types.network_traffic_rule_list

        out["rules"] = (
            aws_sdk_securityagent.types.network_traffic_rule_list.serialize_json(
                value["rules"]
            )
        )
    if "custom_headers" in value:
        import aws_sdk_securityagent.types.custom_header_list

        out["customHeaders"] = (
            aws_sdk_securityagent.types.custom_header_list.serialize_json(
                value["custom_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkTrafficConfig:
    out: NetworkTrafficConfig = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import aws_sdk_securityagent.types.network_traffic_rule_list

        out["rules"] = (
            aws_sdk_securityagent.types.network_traffic_rule_list.deserialize_json(
                data["rules"]
            )
        )
    if "customHeaders" in data:
        import aws_sdk_securityagent.types.custom_header_list

        out["custom_headers"] = (
            aws_sdk_securityagent.types.custom_header_list.deserialize_json(
                data["customHeaders"]
            )
        )
    return out
