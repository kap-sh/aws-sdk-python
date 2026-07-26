"""Generated from Smithy shape ``com.amazonaws.datazone#GetRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.revision
    import capo_datazone.types.rule_id


class GetRuleInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the <code>GetRule</code> action is to be invoked.</p>"""
    identifier: "capo_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuleInput:
    out: GetRuleInput = {}  # type: ignore[typeddict-item]
    return out
