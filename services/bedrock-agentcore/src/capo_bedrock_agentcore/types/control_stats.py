"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ControlStats``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class ControlStats(TypedDict, closed=True):
    variant_name: "str"
    """<p>The name of the control variant.</p>"""
    sample_size: "int"
    """<p>The number of sessions evaluated for the control variant.</p>"""
    mean: "float"
    """<p>The mean evaluation score for the control variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlStats) -> dict:
    out: dict = {}
    out["variantName"] = value["variant_name"]
    out["sampleSize"] = value["sample_size"]
    out["mean"] = value["mean"]
    return out


def deserialize_json(data: dict) -> ControlStats:
    out: ControlStats = {}  # type: ignore[typeddict-item]
    if "variantName" in data:
        out["variant_name"] = data["variantName"]
    else:
        raise DeserializationError("ControlStats.variant_name required")
    if "sampleSize" in data:
        out["sample_size"] = data["sampleSize"]
    else:
        raise DeserializationError("ControlStats.sample_size required")
    if "mean" in data:
        out["mean"] = data["mean"]
    else:
        raise DeserializationError("ControlStats.mean required")
    return out
