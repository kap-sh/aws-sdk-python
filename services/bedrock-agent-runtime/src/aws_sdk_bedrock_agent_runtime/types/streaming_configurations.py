"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StreamingConfigurations``."""

from typing import TypedDict

from typing_extensions import NotRequired


class StreamingConfigurations(TypedDict):
    stream_final_response: "bool"
    """<p> Specifies whether to enable streaming for the final response. This is set to <code>false</code> by default. </p>"""
    apply_guardrail_interval: NotRequired["int"]
    """<p> The guardrail interval to apply as response is generated. By default, the guardrail interval is set to 50 characters. If a larger interval is specified, the response will be generated in larger chunks with fewer <code>ApplyGuardrail</code> calls. The following examples show the response generated for <i>Hello, I am an agent</i> input string.</p> <p> <b>Example response in chunks: Interval set to 3 characters</b> </p> <p> <code>'Hel', 'lo, ','I am', ' an', ' Age', 'nt'</code> </p> <p>Each chunk has at least 3 characters except for the last chunk</p> <p> <b>Example response in chunks: Interval set to 20 or more characters</b> </p> <p> <code>Hello, I am an Agent</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingConfigurations) -> dict:
    out: dict = {}
    out["streamFinalResponse"] = value.get("stream_final_response", False)
    if "apply_guardrail_interval" in value:
        out["applyGuardrailInterval"] = value["apply_guardrail_interval"]
    return out


def deserialize_json(data: dict) -> StreamingConfigurations:
    out: StreamingConfigurations = {}  # type: ignore[typeddict-item]
    if "streamFinalResponse" in data:
        out["stream_final_response"] = data["streamFinalResponse"]
    else:
        out["stream_final_response"] = False
    if "applyGuardrailInterval" in data:
        out["apply_guardrail_interval"] = data["applyGuardrailInterval"]
    return out
