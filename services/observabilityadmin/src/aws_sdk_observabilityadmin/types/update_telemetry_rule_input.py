"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateTelemetryRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.rule_identifier
    import aws_sdk_observabilityadmin.types.telemetry_rule


class UpdateTelemetryRuleInput(TypedDict):
    rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p> The identifier (name or ARN) of the telemetry rule to update. </p>"""
    rule: "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule"
    """<p> The new configuration details for the telemetry rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTelemetryRuleInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    import aws_sdk_observabilityadmin.types.telemetry_rule

    out["Rule"] = aws_sdk_observabilityadmin.types.telemetry_rule.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTelemetryRuleInput:
    out: UpdateTelemetryRuleInput = {}  # type: ignore[typeddict-item]
    if "RuleIdentifier" in data:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError("UpdateTelemetryRuleInput.rule_identifier required")
    if "Rule" in data:
        import aws_sdk_observabilityadmin.types.telemetry_rule

        out["rule"] = aws_sdk_observabilityadmin.types.telemetry_rule.deserialize_json(
            data["Rule"]
        )
    else:
        raise DeserializationError("UpdateTelemetryRuleInput.rule required")
    return out
