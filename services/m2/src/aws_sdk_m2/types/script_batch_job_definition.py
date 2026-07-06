"""Generated from Smithy shape ``com.amazonaws.m2#ScriptBatchJobDefinition``."""

from typing_extensions import TypedDict

from aws_sdk_m2.errors import DeserializationError


class ScriptBatchJobDefinition(TypedDict, closed=True):
    script_name: "str"
    """<p>The name of the script containing the batch job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScriptBatchJobDefinition) -> dict:
    out: dict = {}
    out["scriptName"] = value["script_name"]
    return out


def deserialize_json(data: dict) -> ScriptBatchJobDefinition:
    out: ScriptBatchJobDefinition = {}  # type: ignore[typeddict-item]
    if "scriptName" in data:
        out["script_name"] = data["scriptName"]
    else:
        raise DeserializationError("ScriptBatchJobDefinition.script_name required")
    return out
