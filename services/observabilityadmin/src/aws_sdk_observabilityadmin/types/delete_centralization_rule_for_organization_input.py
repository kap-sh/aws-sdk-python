"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DeleteCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.rule_identifier


class DeleteCentralizationRuleForOrganizationInput(TypedDict, closed=True):
    rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p>The identifier (name or ARN) of the organization centralization rule to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteCentralizationRuleForOrganizationInput:
    out: DeleteCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleIdentifier" in data:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError(
            "DeleteCentralizationRuleForOrganizationInput.rule_identifier required"
        )
    return out
