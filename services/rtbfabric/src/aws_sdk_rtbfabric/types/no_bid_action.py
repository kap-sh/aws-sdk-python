"""Generated from Smithy shape ``com.amazonaws.rtbfabric#NoBidAction``."""

from typing import TypedDict

from typing_extensions import NotRequired


class NoBidAction(TypedDict):
    no_bid_reason_code: NotRequired["int"]
    """<p>The reason code for the no bid action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoBidAction) -> dict:
    out: dict = {}
    if "no_bid_reason_code" in value:
        out["noBidReasonCode"] = value["no_bid_reason_code"]
    return out


def deserialize_json(data: dict) -> NoBidAction:
    out: NoBidAction = {}  # type: ignore[typeddict-item]
    if "noBidReasonCode" in data:
        out["no_bid_reason_code"] = data["noBidReasonCode"]
    return out
