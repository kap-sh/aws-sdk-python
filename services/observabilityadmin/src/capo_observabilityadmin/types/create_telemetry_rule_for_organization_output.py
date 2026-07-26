"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateTelemetryRuleForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn


class CreateTelemetryRuleForOrganizationOutput(TypedDict, closed=True):
    rule_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the created organization telemetry rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTelemetryRuleForOrganizationOutput) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> CreateTelemetryRuleForOrganizationOutput:
    out: CreateTelemetryRuleForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
