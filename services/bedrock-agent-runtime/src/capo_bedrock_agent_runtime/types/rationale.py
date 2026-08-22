"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Rationale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rationale_string
    import capo_bedrock_agent_runtime.types.trace_id


class Rationale(TypedDict, closed=True):
    trace_id: NotRequired["capo_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace step.</p>"""
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.rationale_string.RationaleString"
    ]
    """<p>The reasoning or thought process of the agent, based on the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rationale) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> Rationale:
    out: Rationale = {}  # type: ignore[typeddict-item]
    if data.get("traceId") is not None:
        out["trace_id"] = data["traceId"]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
