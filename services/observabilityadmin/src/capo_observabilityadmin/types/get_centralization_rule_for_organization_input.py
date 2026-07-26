"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.rule_identifier


class GetCentralizationRuleForOrganizationInput(TypedDict, closed=True):
    rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p>The identifier (name or ARN) of the organization centralization rule to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    return out


def deserialize_json(data: dict) -> GetCentralizationRuleForOrganizationInput:
    out: GetCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleIdentifier" in data:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError(
            "GetCentralizationRuleForOrganizationInput.rule_identifier required"
        )
    return out
