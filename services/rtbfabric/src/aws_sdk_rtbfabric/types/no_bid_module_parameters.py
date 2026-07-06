"""Generated from Smithy shape ``com.amazonaws.rtbfabric#NoBidModuleParameters``."""

from typing_extensions import NotRequired, TypedDict


class NoBidModuleParameters(TypedDict, closed=True):
    reason: NotRequired["str"]
    """<p>The reason description.</p>"""
    reason_code: NotRequired["int"]
    """<p>The reason code.</p>"""
    pass_through_percentage: NotRequired["float"]
    """<p>The pass through percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoBidModuleParameters) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "reason_code" in value:
        out["reasonCode"] = value["reason_code"]
    if "pass_through_percentage" in value:
        out["passThroughPercentage"] = value["pass_through_percentage"]
    return out


def deserialize_json(data: dict) -> NoBidModuleParameters:
    out: NoBidModuleParameters = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "reasonCode" in data:
        out["reason_code"] = data["reasonCode"]
    if "passThroughPercentage" in data:
        out["pass_through_percentage"] = data["passThroughPercentage"]
    return out
