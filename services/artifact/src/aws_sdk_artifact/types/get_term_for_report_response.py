"""Generated from Smithy shape ``com.amazonaws.artifact#GetTermForReportResponse``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GetTermForReportResponse(TypedDict):
    document_presigned_url: NotRequired["str"]
    """<p>Presigned S3 url to access the term content.</p>"""
    term_token: NotRequired["str"]
    """<p>Unique token representing this request event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTermForReportResponse) -> dict:
    out: dict = {}
    if "document_presigned_url" in value:
        out["documentPresignedUrl"] = value["document_presigned_url"]
    if "term_token" in value:
        out["termToken"] = value["term_token"]
    return out


def deserialize_json(data: dict) -> GetTermForReportResponse:
    out: GetTermForReportResponse = {}  # type: ignore[typeddict-item]
    if "documentPresignedUrl" in data:
        out["document_presigned_url"] = data["documentPresignedUrl"]
    if "termToken" in data:
        out["term_token"] = data["termToken"]
    return out
