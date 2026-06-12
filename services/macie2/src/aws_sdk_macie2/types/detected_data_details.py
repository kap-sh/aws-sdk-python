"""Generated from Smithy shape ``com.amazonaws.macie2#DetectedDataDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string_min1_max128


class DetectedDataDetails(TypedDict):
    value: NotRequired["aws_sdk_macie2.types.__string_min1_max128.__stringMin1Max128"]
    """<p>An occurrence of the specified type of sensitive data. Each occurrence contains 1-128 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectedDataDetails) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> DetectedDataDetails:
    out: DetectedDataDetails = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    return out
