"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookExportError``."""

from typing import TypedDict
from aws_sdk_datazone.errors import DeserializationError


class NotebookExportError(TypedDict):
    message: "str"
    """<p>The error message. The maximum length is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookExportError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotebookExportError:
    out: NotebookExportError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotebookExportError.message required")
    return out
