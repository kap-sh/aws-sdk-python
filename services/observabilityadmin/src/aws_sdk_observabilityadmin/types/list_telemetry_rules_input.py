"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTelemetryRulesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_max_results
    import aws_sdk_observabilityadmin.types.next_token


class ListTelemetryRulesInput(TypedDict):
    rule_name_prefix: NotRequired["str"]
    """<p> A string to filter telemetry rules whose names begin with the specified prefix. </p>"""
    max_results: NotRequired[
        "aws_sdk_observabilityadmin.types.list_telemetry_rules_max_results.ListTelemetryRulesMaxResults"
    ]
    """<p> The maximum number of telemetry rules to return in a single call. </p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p> The token for the next set of results. A previous call generates this token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTelemetryRulesInput) -> dict:
    out: dict = {}
    if "rule_name_prefix" in value:
        out["RuleNamePrefix"] = value["rule_name_prefix"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTelemetryRulesInput:
    out: ListTelemetryRulesInput = {}  # type: ignore[typeddict-item]
    if "RuleNamePrefix" in data:
        out["rule_name_prefix"] = data["RuleNamePrefix"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
