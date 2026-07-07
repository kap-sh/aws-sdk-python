"""Generated from Smithy shape ``com.amazonaws.sfn#MapStateStartedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.unsigned_integer


class MapStateStartedEventDetails(TypedDict, closed=True):
    length: "aws_sdk_sfn.types.unsigned_integer.UnsignedInteger"
    """<p>The size of the array for Map state iterations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapStateStartedEventDetails) -> dict:
    out: dict = {}
    out["length"] = value.get("length", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> MapStateStartedEventDetails:
    out: MapStateStartedEventDetails = {}  # type: ignore[typeddict-item]
    if "length" in data:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    return out
