"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentError``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError


class EnvironmentError(TypedDict):
    code: NotRequired["str"]
    """<p>The error code for the failure reason for the environment deployment.</p>"""
    message: "str"
    """<p>The error message for the failure reason for the environment deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EnvironmentError:
    out: EnvironmentError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("EnvironmentError.message required")
    return out
