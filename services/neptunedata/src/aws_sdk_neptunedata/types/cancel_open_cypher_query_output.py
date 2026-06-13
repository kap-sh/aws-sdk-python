"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelOpenCypherQueryOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CancelOpenCypherQueryOutput(TypedDict):
    status: NotRequired["str"]
    """<p>The cancellation status of the openCypher query.</p>"""
    payload: NotRequired["bool"]
    """<p>The cancelation payload for the openCypher query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelOpenCypherQueryOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "payload" in value:
        out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> CancelOpenCypherQueryOutput:
    out: CancelOpenCypherQueryOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "payload" in data:
        out["payload"] = data["payload"]
    return out
