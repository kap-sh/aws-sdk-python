"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunError``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class JobRunError(TypedDict, closed=True):
    message: "str"
    """<p>The job run error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> JobRunError:
    out: JobRunError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("JobRunError.message required")
    return out
