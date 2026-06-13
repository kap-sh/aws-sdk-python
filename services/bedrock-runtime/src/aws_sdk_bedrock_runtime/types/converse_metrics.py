"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseMetrics``."""

from typing import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError


class ConverseMetrics(TypedDict):
    latency_ms: "int"
    """<p>The latency of the call to <code>Converse</code>, in milliseconds. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseMetrics) -> dict:
    out: dict = {}
    out["latencyMs"] = value["latency_ms"]
    return out


def deserialize_json(data: dict) -> ConverseMetrics:
    out: ConverseMetrics = {}  # type: ignore[typeddict-item]
    if "latencyMs" in data:
        out["latency_ms"] = data["latencyMs"]
    else:
        raise DeserializationError("ConverseMetrics.latency_ms required")
    return out
