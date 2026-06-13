"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryError``."""

from typing import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class ProtectedQueryError(TypedDict):
    message: "str"
    """<p>A description of why the query failed.</p>"""
    code: "str"
    """<p>An error code for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryError:
    out: ProtectedQueryError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ProtectedQueryError.message required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ProtectedQueryError.code required")
    return out
