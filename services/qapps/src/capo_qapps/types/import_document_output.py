"""Generated from Smithy shape ``com.amazonaws.qapps#ImportDocumentOutput``."""

from typing_extensions import NotRequired, TypedDict


class ImportDocumentOutput(TypedDict, closed=True):
    file_id: NotRequired["str"]
    """<p>The unique identifier assigned to the uploaded file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDocumentOutput) -> dict:
    out: dict = {}
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    return out


def deserialize_json(data: dict) -> ImportDocumentOutput:
    out: ImportDocumentOutput = {}  # type: ignore[typeddict-item]
    if "fileId" in data:
        out["file_id"] = data["fileId"]
    return out
