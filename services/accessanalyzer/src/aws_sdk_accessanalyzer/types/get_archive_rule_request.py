"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetArchiveRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_name
    import aws_sdk_accessanalyzer.types.name


class GetArchiveRuleRequest(TypedDict, closed=True):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to retrieve rules from.</p>"""
    rule_name: "aws_sdk_accessanalyzer.types.name.Name"
    """<p>The name of the rule to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArchiveRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetArchiveRuleRequest:
    out: GetArchiveRuleRequest = {}  # type: ignore[typeddict-item]
    return out
