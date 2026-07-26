"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CategoricalScaleDefinition``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError


class CategoricalScaleDefinition(TypedDict, closed=True):
    definition: "str"
    """<p> The description that explains what this categorical rating represents and when it should be used. </p>"""
    label: "str"
    """<p> The label or name of this categorical rating option. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoricalScaleDefinition) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> CategoricalScaleDefinition:
    out: CategoricalScaleDefinition = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("CategoricalScaleDefinition.definition required")
    if "label" in data:
        out["label"] = data["label"]
    else:
        raise DeserializationError("CategoricalScaleDefinition.label required")
    return out
