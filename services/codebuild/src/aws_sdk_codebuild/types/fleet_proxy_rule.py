"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_proxy_rule_effect_type
    import aws_sdk_codebuild.types.fleet_proxy_rule_entities
    import aws_sdk_codebuild.types.fleet_proxy_rule_type


class FleetProxyRule(TypedDict):
    type: "aws_sdk_codebuild.types.fleet_proxy_rule_type.FleetProxyRuleType"
    """<p>The type of proxy rule.</p>"""
    effect: (
        "aws_sdk_codebuild.types.fleet_proxy_rule_effect_type.FleetProxyRuleEffectType"
    )
    """<p>The behavior of the proxy rule.</p>"""
    entities: "aws_sdk_codebuild.types.fleet_proxy_rule_entities.FleetProxyRuleEntities"
    """<p>The destination of the proxy rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRule) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.fleet_proxy_rule_type

    out["type"] = aws_sdk_codebuild.types.fleet_proxy_rule_type.serialize_aws_json_1_1(
        value["type"]
    )
    import aws_sdk_codebuild.types.fleet_proxy_rule_effect_type

    out["effect"] = (
        aws_sdk_codebuild.types.fleet_proxy_rule_effect_type.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    import aws_sdk_codebuild.types.fleet_proxy_rule_entities

    out["entities"] = (
        aws_sdk_codebuild.types.fleet_proxy_rule_entities.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetProxyRule:
    out: FleetProxyRule = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_codebuild.types.fleet_proxy_rule_type

        out["type"] = (
            aws_sdk_codebuild.types.fleet_proxy_rule_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        raise DeserializationError("FleetProxyRule.type required")
    if "effect" in data:
        import aws_sdk_codebuild.types.fleet_proxy_rule_effect_type

        out["effect"] = (
            aws_sdk_codebuild.types.fleet_proxy_rule_effect_type.deserialize_aws_json_1_1(
                data["effect"]
            )
        )
    else:
        raise DeserializationError("FleetProxyRule.effect required")
    if "entities" in data:
        import aws_sdk_codebuild.types.fleet_proxy_rule_entities

        out["entities"] = (
            aws_sdk_codebuild.types.fleet_proxy_rule_entities.deserialize_aws_json_1_1(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("FleetProxyRule.entities required")
    return out
