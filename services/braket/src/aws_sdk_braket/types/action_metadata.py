"""Generated from Smithy shape ``com.amazonaws.braket#ActionMetadata``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError


class ActionMetadata(TypedDict):
    action_type: "str"
    """<p>The type of action associated with the quantum task.</p>"""
    program_count: NotRequired["int"]
    """<p>The number of programs in a program set. This is only available for a program set.</p>"""
    executable_count: NotRequired["int"]
    """<p>The number of executables in a program set. This is only available for a program set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionMetadata) -> dict:
    out: dict = {}
    out["actionType"] = value["action_type"]
    if "program_count" in value:
        out["programCount"] = value["program_count"]
    if "executable_count" in value:
        out["executableCount"] = value["executable_count"]
    return out


def deserialize_json(data: dict) -> ActionMetadata:
    out: ActionMetadata = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        out["action_type"] = data["actionType"]
    else:
        raise DeserializationError("ActionMetadata.action_type required")
    if "programCount" in data:
        out["program_count"] = data["programCount"]
    if "executableCount" in data:
        out["executable_count"] = data["executableCount"]
    return out
