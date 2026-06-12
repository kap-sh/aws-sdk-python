"""Generated from Smithy shape ``com.amazonaws.oam#GetSinkPolicyOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GetSinkPolicyOutput(TypedDict):
    sink_arn: NotRequired["str"]
    """<p>The ARN of the sink.</p>"""
    sink_id: NotRequired["str"]
    """<p>The random ID string that Amazon Web Services generated as part of the sink ARN.</p>"""
    policy: NotRequired["str"]
    """<p>The policy that you specified, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSinkPolicyOutput) -> dict:
    out: dict = {}
    if "sink_arn" in value:
        out["SinkArn"] = value["sink_arn"]
    if "sink_id" in value:
        out["SinkId"] = value["sink_id"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetSinkPolicyOutput:
    out: GetSinkPolicyOutput = {}  # type: ignore[typeddict-item]
    if "SinkArn" in data:
        out["sink_arn"] = data["SinkArn"]
    if "SinkId" in data:
        out["sink_id"] = data["SinkId"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
