"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.evidence


class GetEvidenceResponse(TypedDict):
    evidence: NotRequired["aws_sdk_auditmanager.types.evidence.Evidence"]
    """<p> The evidence that the <code>GetEvidence</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceResponse) -> dict:
    out: dict = {}
    if "evidence" in value:
        import aws_sdk_auditmanager.types.evidence

        out["evidence"] = aws_sdk_auditmanager.types.evidence.serialize_json(
            value["evidence"]
        )
    return out


def deserialize_json(data: dict) -> GetEvidenceResponse:
    out: GetEvidenceResponse = {}  # type: ignore[typeddict-item]
    if "evidence" in data:
        import aws_sdk_auditmanager.types.evidence

        out["evidence"] = aws_sdk_auditmanager.types.evidence.deserialize_json(
            data["evidence"]
        )
    return out
