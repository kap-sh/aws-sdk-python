"""Generated from Smithy shape ``com.amazonaws.artifact#GetReportResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetReportResponse(TypedDict, closed=True):
    document_presigned_url: NotRequired["str"]
    """<p>Presigned S3 url to access the report content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportResponse) -> dict:
    out: dict = {}
    if "document_presigned_url" in value:
        out["documentPresignedUrl"] = value["document_presigned_url"]
    return out


def deserialize_json(data: dict) -> GetReportResponse:
    out: GetReportResponse = {}  # type: ignore[typeddict-item]
    if "documentPresignedUrl" in data:
        out["document_presigned_url"] = data["documentPresignedUrl"]
    return out
