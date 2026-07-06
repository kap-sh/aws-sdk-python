"""Generated from Smithy shape ``com.amazonaws.deadline#ConsumedUsages``."""

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError


class ConsumedUsages(TypedDict, closed=True):
    approximate_dollar_usage: "float"
    """<p>The amount of the budget consumed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumedUsages) -> dict:
    out: dict = {}
    out["approximateDollarUsage"] = value["approximate_dollar_usage"]
    return out


def deserialize_json(data: dict) -> ConsumedUsages:
    out: ConsumedUsages = {}  # type: ignore[typeddict-item]
    if "approximateDollarUsage" in data:
        out["approximate_dollar_usage"] = data["approximateDollarUsage"]
    else:
        raise DeserializationError("ConsumedUsages.approximate_dollar_usage required")
    return out
