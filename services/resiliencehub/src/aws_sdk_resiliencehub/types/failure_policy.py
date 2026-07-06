"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FailurePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.seconds


class FailurePolicy(TypedDict, closed=True):
    rto_in_secs: "aws_sdk_resiliencehub.types.seconds.Seconds"
    """<p>Recovery Time Objective (RTO) in seconds.</p>"""
    rpo_in_secs: "aws_sdk_resiliencehub.types.seconds.Seconds"
    """<p>Recovery Point Objective (RPO) in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailurePolicy) -> dict:
    out: dict = {}
    out["rtoInSecs"] = value.get("rto_in_secs", 0)
    out["rpoInSecs"] = value.get("rpo_in_secs", 0)
    return out


def deserialize_json(data: dict) -> FailurePolicy:
    out: FailurePolicy = {}  # type: ignore[typeddict-item]
    if "rtoInSecs" in data:
        out["rto_in_secs"] = data["rtoInSecs"]
    else:
        out["rto_in_secs"] = 0
    if "rpoInSecs" in data:
        out["rpo_in_secs"] = data["rpoInSecs"]
    else:
        out["rpo_in_secs"] = 0
    return out
