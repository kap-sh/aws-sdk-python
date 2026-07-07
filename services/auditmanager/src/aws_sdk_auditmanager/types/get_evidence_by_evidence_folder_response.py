"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceByEvidenceFolderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.evidence_list
    import aws_sdk_auditmanager.types.token


class GetEvidenceByEvidenceFolderResponse(TypedDict, closed=True):
    evidence: NotRequired["aws_sdk_auditmanager.types.evidence_list.EvidenceList"]
    """<p> The list of evidence that the <code>GetEvidenceByEvidenceFolder</code> API returned. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceByEvidenceFolderResponse) -> dict:
    out: dict = {}
    if "evidence" in value:
        import aws_sdk_auditmanager.types.evidence_list

        out["evidence"] = aws_sdk_auditmanager.types.evidence_list.serialize_json(
            value["evidence"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEvidenceByEvidenceFolderResponse:
    out: GetEvidenceByEvidenceFolderResponse = {}  # type: ignore[typeddict-item]
    if "evidence" in data:
        import aws_sdk_auditmanager.types.evidence_list

        out["evidence"] = aws_sdk_auditmanager.types.evidence_list.deserialize_json(
            data["evidence"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
