"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentReportUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.url


class GetAssessmentReportUrlResponse(TypedDict, closed=True):
    pre_signed_url: NotRequired["capo_auditmanager.types.url.URL"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentReportUrlResponse) -> dict:
    out: dict = {}
    if "pre_signed_url" in value:
        import capo_auditmanager.types.url

        out["preSignedUrl"] = capo_auditmanager.types.url.serialize_json(
            value["pre_signed_url"]
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentReportUrlResponse:
    out: GetAssessmentReportUrlResponse = {}  # type: ignore[typeddict-item]
    if "preSignedUrl" in data:
        import capo_auditmanager.types.url

        out["pre_signed_url"] = capo_auditmanager.types.url.deserialize_json(
            data["preSignedUrl"]
        )
    return out
