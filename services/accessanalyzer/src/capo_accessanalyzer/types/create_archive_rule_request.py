"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateArchiveRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_name
    import capo_accessanalyzer.types.filter_criteria_map
    import capo_accessanalyzer.types.name


class CreateArchiveRuleRequest(TypedDict, closed=True):
    analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the created analyzer.</p>"""
    rule_name: "capo_accessanalyzer.types.name.Name"
    """<p>The name of the rule to create.</p>"""
    filter: "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    """<p>The criteria for the rule.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateArchiveRuleRequest) -> dict:
    out: dict = {}
    out["ruleName"] = value["rule_name"]
    import capo_accessanalyzer.types.filter_criteria_map

    out["filter"] = capo_accessanalyzer.types.filter_criteria_map.serialize_json(
        value["filter"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateArchiveRuleRequest:
    out: CreateArchiveRuleRequest = {}  # type: ignore[typeddict-item]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("CreateArchiveRuleRequest.rule_name required")
    if "filter" in data:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.deserialize_json(
            data["filter"]
        )
    else:
        raise DeserializationError("CreateArchiveRuleRequest.filter required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
