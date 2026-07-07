"""Generated from Smithy shape ``com.amazonaws.codebuild#ProxyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_proxy_rule_behavior
    import aws_sdk_codebuild.types.fleet_proxy_rules


class ProxyConfiguration(TypedDict, closed=True):
    default_behavior: NotRequired[
        "aws_sdk_codebuild.types.fleet_proxy_rule_behavior.FleetProxyRuleBehavior"
    ]
    """<p>The default behavior of outgoing traffic.</p>"""
    ordered_proxy_rules: NotRequired[
        "aws_sdk_codebuild.types.fleet_proxy_rules.FleetProxyRules"
    ]
    """<p>An array of <code>FleetProxyRule</code> objects that represent the specified destination domains or IPs to allow or deny network access control to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfiguration) -> dict:
    out: dict = {}
    if "default_behavior" in value:
        import aws_sdk_codebuild.types.fleet_proxy_rule_behavior

        out["defaultBehavior"] = (
            aws_sdk_codebuild.types.fleet_proxy_rule_behavior.serialize_aws_json_1_1(
                value["default_behavior"]
            )
        )
    if "ordered_proxy_rules" in value:
        import aws_sdk_codebuild.types.fleet_proxy_rules

        out["orderedProxyRules"] = (
            aws_sdk_codebuild.types.fleet_proxy_rules.serialize_aws_json_1_1(
                value["ordered_proxy_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if "defaultBehavior" in data:
        import aws_sdk_codebuild.types.fleet_proxy_rule_behavior

        out["default_behavior"] = (
            aws_sdk_codebuild.types.fleet_proxy_rule_behavior.deserialize_aws_json_1_1(
                data["defaultBehavior"]
            )
        )
    if "orderedProxyRules" in data:
        import aws_sdk_codebuild.types.fleet_proxy_rules

        out["ordered_proxy_rules"] = (
            aws_sdk_codebuild.types.fleet_proxy_rules.deserialize_aws_json_1_1(
                data["orderedProxyRules"]
            )
        )
    return out
