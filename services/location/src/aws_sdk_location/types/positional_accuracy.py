"""Generated from Smithy shape ``com.amazonaws.location#PositionalAccuracy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.sensitive_double


class PositionalAccuracy(TypedDict, closed=True):
    horizontal: "aws_sdk_location.types.sensitive_double.SensitiveDouble"
    """<p>Estimated maximum distance, in meters, between the measured position and the true position of a device, along the Earth's surface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionalAccuracy) -> dict:
    out: dict = {}
    out["Horizontal"] = value["horizontal"]
    return out


def deserialize_json(data: dict) -> PositionalAccuracy:
    out: PositionalAccuracy = {}  # type: ignore[typeddict-item]
    if "Horizontal" in data:
        out["horizontal"] = data["Horizontal"]
    else:
        raise DeserializationError("PositionalAccuracy.horizontal required")
    return out
