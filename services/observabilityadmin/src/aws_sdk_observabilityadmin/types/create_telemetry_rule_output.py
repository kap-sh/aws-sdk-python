"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateTelemetryRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn


class CreateTelemetryRuleOutput(TypedDict, closed=True):
    rule_arn: NotRequired["aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the created telemetry rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTelemetryRuleOutput) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> CreateTelemetryRuleOutput:
    out: CreateTelemetryRuleOutput = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
