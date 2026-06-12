"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.centralization_rule
    import aws_sdk_observabilityadmin.types.rule_identifier


class UpdateCentralizationRuleForOrganizationInput(TypedDict):
    rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p>The identifier (name or ARN) of the organization centralization rule to update.</p>"""
    rule: "aws_sdk_observabilityadmin.types.centralization_rule.CentralizationRule"
    """<p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    import aws_sdk_observabilityadmin.types.centralization_rule

    out["Rule"] = aws_sdk_observabilityadmin.types.centralization_rule.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCentralizationRuleForOrganizationInput:
    out: UpdateCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleIdentifier" in data:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError(
            "UpdateCentralizationRuleForOrganizationInput.rule_identifier required"
        )
    if "Rule" in data:
        import aws_sdk_observabilityadmin.types.centralization_rule

        out["rule"] = (
            aws_sdk_observabilityadmin.types.centralization_rule.deserialize_json(
                data["Rule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCentralizationRuleForOrganizationInput.rule required"
        )
    return out
