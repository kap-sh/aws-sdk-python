"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#DeleteArchiveRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_name
    import capo_accessanalyzer.types.name


class DeleteArchiveRuleRequest(TypedDict, closed=True):
    analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer that associated with the archive rule to delete.</p>"""
    rule_name: "capo_accessanalyzer.types.name.Name"
    """<p>The name of the rule to delete.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteArchiveRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteArchiveRuleRequest:
    out: DeleteArchiveRuleRequest = {}  # type: ignore[typeddict-item]
    return out
