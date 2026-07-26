"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetTelemetryRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.rule_identifier


class GetTelemetryRuleForOrganizationInput(TypedDict, closed=True):
    rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p> The identifier (name or ARN) of the organization telemetry rule to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTelemetryRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    return out


def deserialize_json(data: dict) -> GetTelemetryRuleForOrganizationInput:
    out: GetTelemetryRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleIdentifier" in data:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError(
            "GetTelemetryRuleForOrganizationInput.rule_identifier required"
        )
    return out
