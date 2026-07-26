"""Generated from Smithy shape ``com.amazonaws.pipes#BatchEnvironmentVariable``."""

from typing_extensions import NotRequired, TypedDict


class BatchEnvironmentVariable(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the key-value pair. For environment variables, this is the name of the environment variable.</p>"""
    value: NotRequired["str"]
    """<p>The value of the key-value pair. For environment variables, this is the value of the environment variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnvironmentVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> BatchEnvironmentVariable:
    out: BatchEnvironmentVariable = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
