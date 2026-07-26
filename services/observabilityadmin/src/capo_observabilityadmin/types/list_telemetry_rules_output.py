"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTelemetryRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.telemetry_rule_summaries


class ListTelemetryRulesOutput(TypedDict, closed=True):
    telemetry_rule_summaries: NotRequired[
        "capo_observabilityadmin.types.telemetry_rule_summaries.TelemetryRuleSummaries"
    ]
    """<p> A list of telemetry rule summaries. </p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p> A token to resume pagination of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTelemetryRulesOutput) -> dict:
    out: dict = {}
    if "telemetry_rule_summaries" in value:
        import capo_observabilityadmin.types.telemetry_rule_summaries

        out["TelemetryRuleSummaries"] = (
            capo_observabilityadmin.types.telemetry_rule_summaries.serialize_json(
                value["telemetry_rule_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTelemetryRulesOutput:
    out: ListTelemetryRulesOutput = {}  # type: ignore[typeddict-item]
    if "TelemetryRuleSummaries" in data:
        import capo_observabilityadmin.types.telemetry_rule_summaries

        out["telemetry_rule_summaries"] = (
            capo_observabilityadmin.types.telemetry_rule_summaries.deserialize_json(
                data["TelemetryRuleSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
