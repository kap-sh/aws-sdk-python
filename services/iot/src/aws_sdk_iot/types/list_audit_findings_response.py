"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditFindingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_findings
    import aws_sdk_iot.types.next_token


class ListAuditFindingsResponse(TypedDict):
    findings: NotRequired["aws_sdk_iot.types.audit_findings.AuditFindings"]
    """<p>The findings (results) of the audit.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditFindingsResponse) -> dict:
    out: dict = {}
    if "findings" in value:
        import aws_sdk_iot.types.audit_findings

        out["findings"] = aws_sdk_iot.types.audit_findings.serialize_json(
            value["findings"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditFindingsResponse:
    out: ListAuditFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_iot.types.audit_findings

        out["findings"] = aws_sdk_iot.types.audit_findings.deserialize_json(
            data["findings"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
