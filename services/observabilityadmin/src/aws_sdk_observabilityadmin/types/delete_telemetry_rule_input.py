"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DeleteTelemetryRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.rule_identifier


class DeleteTelemetryRuleInput(TypedDict):
    rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p> The identifier (name or ARN) of the telemetry rule to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTelemetryRuleInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteTelemetryRuleInput:
    out: DeleteTelemetryRuleInput = {}  # type: ignore[typeddict-item]
    if "RuleIdentifier" in data:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError("DeleteTelemetryRuleInput.rule_identifier required")
    return out
