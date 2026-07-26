"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookError``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class NotebookError(TypedDict, closed=True):
    message: "str"
    """<p>The error message. The maximum length is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotebookError:
    out: NotebookError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotebookError.message required")
    return out
