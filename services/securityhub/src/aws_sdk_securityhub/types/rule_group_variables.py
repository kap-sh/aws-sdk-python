"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupVariables``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_variables_ip_sets_details
    import aws_sdk_securityhub.types.rule_group_variables_port_sets_details


class RuleGroupVariables(TypedDict, closed=True):
    ip_sets: NotRequired[
        "aws_sdk_securityhub.types.rule_group_variables_ip_sets_details.RuleGroupVariablesIpSetsDetails"
    ]
    """<p>A list of IP addresses and address ranges, in CIDR notation.</p>"""
    port_sets: NotRequired[
        "aws_sdk_securityhub.types.rule_group_variables_port_sets_details.RuleGroupVariablesPortSetsDetails"
    ]
    """<p>A list of port ranges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupVariables) -> dict:
    out: dict = {}
    if "ip_sets" in value:
        import aws_sdk_securityhub.types.rule_group_variables_ip_sets_details

        out["IpSets"] = (
            aws_sdk_securityhub.types.rule_group_variables_ip_sets_details.serialize_json(
                value["ip_sets"]
            )
        )
    if "port_sets" in value:
        import aws_sdk_securityhub.types.rule_group_variables_port_sets_details

        out["PortSets"] = (
            aws_sdk_securityhub.types.rule_group_variables_port_sets_details.serialize_json(
                value["port_sets"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupVariables:
    out: RuleGroupVariables = {}  # type: ignore[typeddict-item]
    if "IpSets" in data:
        import aws_sdk_securityhub.types.rule_group_variables_ip_sets_details

        out["ip_sets"] = (
            aws_sdk_securityhub.types.rule_group_variables_ip_sets_details.deserialize_json(
                data["IpSets"]
            )
        )
    if "PortSets" in data:
        import aws_sdk_securityhub.types.rule_group_variables_port_sets_details

        out["port_sets"] = (
            aws_sdk_securityhub.types.rule_group_variables_port_sets_details.deserialize_json(
                data["PortSets"]
            )
        )
    return out
