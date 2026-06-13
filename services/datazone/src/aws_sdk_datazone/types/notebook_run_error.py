"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunError``."""

from typing import TypedDict
from aws_sdk_datazone.errors import DeserializationError


class NotebookRunError(TypedDict):
    message: "str"
    """<p>The error message. The maximum length is 1024 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookRunError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotebookRunError:
    out: NotebookRunError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotebookRunError.message required")
    return out
