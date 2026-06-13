"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.metric_name
    import aws_sdk_cleanroomsml.types.metric_regex


class MetricDefinition(TypedDict):
    name: "aws_sdk_cleanroomsml.types.metric_name.MetricName"
    """<p>The name of the model metric.</p>"""
    regex: "aws_sdk_cleanroomsml.types.metric_regex.MetricRegex"
    """<p>The regular expression statement that defines how the model metric is reported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["regex"] = value["regex"]
    return out


def deserialize_json(data: dict) -> MetricDefinition:
    out: MetricDefinition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MetricDefinition.name required")
    if "regex" in data:
        out["regex"] = data["regex"]
    else:
        raise DeserializationError("MetricDefinition.regex required")
    return out
