"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateTelemetryRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn


class UpdateTelemetryRuleOutput(TypedDict):
    rule_arn: NotRequired["aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the updated telemetry rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTelemetryRuleOutput) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> UpdateTelemetryRuleOutput:
    out: UpdateTelemetryRuleOutput = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
