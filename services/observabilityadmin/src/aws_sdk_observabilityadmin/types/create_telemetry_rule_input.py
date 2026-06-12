"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateTelemetryRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.rule_name
    import aws_sdk_observabilityadmin.types.tag_map_input
    import aws_sdk_observabilityadmin.types.telemetry_rule


class CreateTelemetryRuleInput(TypedDict):
    rule_name: "aws_sdk_observabilityadmin.types.rule_name.RuleName"
    """<p> A unique name for the telemetry rule being created. </p>"""
    rule: "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule"
    """<p> The configuration details for the telemetry rule, including the resource type, telemetry type, destination configuration, and selection criteria for which resources the rule applies to. </p>"""
    tags: NotRequired["aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p> The key-value pairs to associate with the telemetry rule resource for categorization and management purposes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTelemetryRuleInput) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    import aws_sdk_observabilityadmin.types.telemetry_rule

    out["Rule"] = aws_sdk_observabilityadmin.types.telemetry_rule.serialize_json(
        value["rule"]
    )
    if "tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateTelemetryRuleInput:
    out: CreateTelemetryRuleInput = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("CreateTelemetryRuleInput.rule_name required")
    if "Rule" in data:
        import aws_sdk_observabilityadmin.types.telemetry_rule

        out["rule"] = aws_sdk_observabilityadmin.types.telemetry_rule.deserialize_json(
            data["Rule"]
        )
    else:
        raise DeserializationError("CreateTelemetryRuleInput.rule required")
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
