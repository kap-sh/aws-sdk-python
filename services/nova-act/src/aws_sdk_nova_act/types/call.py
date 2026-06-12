"""Generated from Smithy shape ``com.amazonaws.novaact#Call``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.call_id
    import aws_sdk_nova_act.types.sensitive_document


class Call(TypedDict):
    call_id: "aws_sdk_nova_act.types.call_id.CallId"
    """<p>A unique identifier for this tool call, used to match results back to requests.</p>"""
    input: "aws_sdk_nova_act.types.sensitive_document.SensitiveDocument"
    """<p>The input parameters for the tool call, formatted according to the tool's schema.</p>"""
    name: "str"
    """<p>The name of the tool to invoke, following the pattern 'tool.{toolName}' or 'browser.{browserAction}'.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Call) -> dict:
    out: dict = {}
    out["callId"] = value["call_id"]
    out["input"] = value["input"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Call:
    out: Call = {}  # type: ignore[typeddict-item]
    if "callId" in data:
        out["call_id"] = data["callId"]
    else:
        raise DeserializationError("Call.call_id required")
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError("Call.input required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Call.name required")
    return out
