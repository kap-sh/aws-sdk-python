"""Generated from Smithy shape ``com.amazonaws.securityagent#VerificationScriptEnvVar``."""

from typing import TypedDict

from typing_extensions import NotRequired


class VerificationScriptEnvVar(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the environment variable.</p>"""
    value: NotRequired["str"]
    """<p>The value of the environment variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerificationScriptEnvVar) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> VerificationScriptEnvVar:
    out: VerificationScriptEnvVar = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
