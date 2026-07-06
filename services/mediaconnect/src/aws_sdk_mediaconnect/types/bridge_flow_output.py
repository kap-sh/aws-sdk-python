"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeFlowOutput``."""

from typing_extensions import NotRequired, TypedDict


class BridgeFlowOutput(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The Amazon Resource Number (ARN) of the cloud flow.</p>"""
    flow_source_arn: NotRequired["str"]
    """<p> The Amazon Resource Number (ARN) of the flow source.</p>"""
    name: NotRequired["str"]
    """<p> The name of the bridge's output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BridgeFlowOutput) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_source_arn" in value:
        out["flowSourceArn"] = value["flow_source_arn"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> BridgeFlowOutput:
    out: BridgeFlowOutput = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowSourceArn" in data:
        out["flow_source_arn"] = data["flowSourceArn"]
    if "name" in data:
        out["name"] = data["name"]
    return out
