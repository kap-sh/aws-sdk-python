"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateCentralizationRuleForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn


class CreateCentralizationRuleForOrganizationOutput(TypedDict, closed=True):
    rule_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the created organization centralization rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCentralizationRuleForOrganizationOutput) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> CreateCentralizationRuleForOrganizationOutput:
    out: CreateCentralizationRuleForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
