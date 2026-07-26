"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobError``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class ProtectedJobError(TypedDict, closed=True):
    message: "str"
    """<p> The message for the protected job error.</p>"""
    code: "str"
    """<p> The error code for the protected job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ProtectedJobError:
    out: ProtectedJobError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ProtectedJobError.message required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ProtectedJobError.code required")
    return out
