"""Generated from Smithy shape ``com.amazonaws.devopsagent#UsageMetric``."""

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class UsageMetric(TypedDict, closed=True):
    limit: "int"
    """<p>Configured limit for this metric. A value of -1 indicates no limit is enforced.</p>"""
    usage: "float"
    """<p>Current usage for this metric</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageMetric) -> dict:
    out: dict = {}
    out["limit"] = value["limit"]
    out["usage"] = value["usage"]
    return out


def deserialize_json(data: dict) -> UsageMetric:
    out: UsageMetric = {}  # type: ignore[typeddict-item]
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        raise DeserializationError("UsageMetric.limit required")
    if "usage" in data:
        out["usage"] = data["usage"]
    else:
        raise DeserializationError("UsageMetric.usage required")
    return out
