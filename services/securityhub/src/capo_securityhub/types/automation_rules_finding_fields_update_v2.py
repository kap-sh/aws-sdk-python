"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesFindingFieldsUpdateV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AutomationRulesFindingFieldsUpdateV2(TypedDict, closed=True):
    severity_id: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The severity level to be assigned to findings that match the automation rule criteria.</p>"""
    comment: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Notes or contextual information for findings that are modified by the automation rule.</p>"""
    status_id: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The status to be applied to findings that match automation rule criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesFindingFieldsUpdateV2) -> dict:
    out: dict = {}
    if "severity_id" in value:
        out["SeverityId"] = value["severity_id"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "status_id" in value:
        out["StatusId"] = value["status_id"]
    return out


def deserialize_json(data: dict) -> AutomationRulesFindingFieldsUpdateV2:
    out: AutomationRulesFindingFieldsUpdateV2 = {}  # type: ignore[typeddict-item]
    if "SeverityId" in data:
        out["severity_id"] = data["SeverityId"]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    if "StatusId" in data:
        out["status_id"] = data["StatusId"]
    return out
