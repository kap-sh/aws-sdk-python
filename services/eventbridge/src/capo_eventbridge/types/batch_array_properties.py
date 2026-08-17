"""Generated from Smithy shape ``com.amazonaws.eventbridge#BatchArrayProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.integer


class BatchArrayProperties(TypedDict, closed=True):
    size: "capo_eventbridge.types.integer.Integer"
    """<p>The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchArrayProperties) -> dict:
    out: dict = {}
    out["Size"] = value.get("size", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchArrayProperties:
    out: BatchArrayProperties = {}  # type: ignore[typeddict-item]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
