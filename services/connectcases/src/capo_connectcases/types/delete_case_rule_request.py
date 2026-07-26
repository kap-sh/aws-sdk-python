"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteCaseRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_id
    import capo_connectcases.types.domain_id


class DeleteCaseRuleRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCaseRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCaseRuleRequest:
    out: DeleteCaseRuleRequest = {}  # type: ignore[typeddict-item]
    return out
