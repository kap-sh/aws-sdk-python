"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationsConfig``."""

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError


class CitationsConfig(TypedDict, closed=True):
    enabled: "bool"
    """<p>Specifies whether citations from the selected document should be used in the model's response. When set to true, the model can generate citations that reference the source documents used to inform the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationsConfig) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> CitationsConfig:
    out: CitationsConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("CitationsConfig.enabled required")
    return out
