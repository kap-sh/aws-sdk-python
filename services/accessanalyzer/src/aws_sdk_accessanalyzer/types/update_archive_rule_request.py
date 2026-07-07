"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UpdateArchiveRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_name
    import aws_sdk_accessanalyzer.types.filter_criteria_map
    import aws_sdk_accessanalyzer.types.name


class UpdateArchiveRuleRequest(TypedDict, closed=True):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to update the archive rules for.</p>"""
    rule_name: "aws_sdk_accessanalyzer.types.name.Name"
    """<p>The name of the rule to update.</p>"""
    filter: "aws_sdk_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    """<p>A filter to match for the rules to update. Only rules that match the filter are updated.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateArchiveRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.filter_criteria_map

    out["filter"] = aws_sdk_accessanalyzer.types.filter_criteria_map.serialize_json(
        value["filter"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateArchiveRuleRequest:
    out: UpdateArchiveRuleRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_accessanalyzer.types.filter_criteria_map

        out["filter"] = (
            aws_sdk_accessanalyzer.types.filter_criteria_map.deserialize_json(
                data["filter"]
            )
        )
    else:
        raise DeserializationError("UpdateArchiveRuleRequest.filter required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
