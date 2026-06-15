"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NumericalScaleDefinition``."""

from typing import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError


class NumericalScaleDefinition(TypedDict):
    definition: "str"
    """<p> The description that explains what this numerical rating represents and when it should be used. </p>"""
    value: "float"
    """<p> The numerical value for this rating scale option. </p>"""
    label: "str"
    """<p> The label or name that describes this numerical rating option. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericalScaleDefinition) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    out["value"] = value["value"]
    out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> NumericalScaleDefinition:
    out: NumericalScaleDefinition = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("NumericalScaleDefinition.definition required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("NumericalScaleDefinition.value required")
    if "label" in data:
        out["label"] = data["label"]
    else:
        raise DeserializationError("NumericalScaleDefinition.label required")
    return out
