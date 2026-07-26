"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_proxy_rule

FleetProxyRules: TypeAlias = list[
    "capo_codebuild.types.fleet_proxy_rule.FleetProxyRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRules) -> list:
    import capo_codebuild.types.fleet_proxy_rule

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.fleet_proxy_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetProxyRules:
    import capo_codebuild.types.fleet_proxy_rule

    out: FleetProxyRules = []
    for item in data:
        out.append(capo_codebuild.types.fleet_proxy_rule.deserialize_aws_json_1_1(item))
    return out
