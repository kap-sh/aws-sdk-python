"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_findings
    import capo_iot.types.next_token


class ListAuditFindingsResponse(TypedDict, closed=True):
    findings: NotRequired["capo_iot.types.audit_findings.AuditFindings"]
    """<p>The findings (results) of the audit.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditFindingsResponse) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_iot.types.audit_findings

        out["findings"] = capo_iot.types.audit_findings.serialize_json(
            value["findings"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditFindingsResponse:
    out: ListAuditFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import capo_iot.types.audit_findings

        out["findings"] = capo_iot.types.audit_findings.deserialize_json(
            data["findings"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
