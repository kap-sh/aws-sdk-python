"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineSummary``."""

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError


class BaselineSummary(TypedDict, closed=True):
    arn: "str"
    """<p>The full ARN of a Baseline.</p>"""
    name: "str"
    """<p>The human-readable name of a Baseline.</p>"""
    description: NotRequired["str"]
    """<p>A summary description of a Baseline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaselineSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BaselineSummary:
    out: BaselineSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("BaselineSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BaselineSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    return out
