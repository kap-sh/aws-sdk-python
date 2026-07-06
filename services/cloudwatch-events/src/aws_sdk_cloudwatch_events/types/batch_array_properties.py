"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#BatchArrayProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.integer


class BatchArrayProperties(TypedDict, closed=True):
    size: "aws_sdk_cloudwatch_events.types.integer.Integer"
    """<p>The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchArrayProperties) -> dict:
    out: dict = {}
    out["Size"] = value.get("size", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchArrayProperties:
    out: BatchArrayProperties = {}  # type: ignore[typeddict-item]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
