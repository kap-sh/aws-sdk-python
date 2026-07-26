"""Generated from Smithy shape ``com.amazonaws.m2#ScriptBatchJobIdentifier``."""

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError


class ScriptBatchJobIdentifier(TypedDict, closed=True):
    script_name: "str"
    """<p>The name of the script containing the batch job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScriptBatchJobIdentifier) -> dict:
    out: dict = {}
    out["scriptName"] = value["script_name"]
    return out


def deserialize_json(data: dict) -> ScriptBatchJobIdentifier:
    out: ScriptBatchJobIdentifier = {}  # type: ignore[typeddict-item]
    if "scriptName" in data:
        out["script_name"] = data["scriptName"]
    else:
        raise DeserializationError("ScriptBatchJobIdentifier.script_name required")
    return out
