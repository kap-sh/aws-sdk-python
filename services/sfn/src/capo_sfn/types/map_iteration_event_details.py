"""Generated from Smithy shape ``com.amazonaws.sfn#MapIterationEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.name
    import capo_sfn.types.unsigned_integer


class MapIterationEventDetails(TypedDict, closed=True):
    name: NotRequired["capo_sfn.types.name.Name"]
    """<p>The name of the iteration’s parent Map state.</p>"""
    index: "capo_sfn.types.unsigned_integer.UnsignedInteger"
    """<p>The index of the array belonging to the Map state iteration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapIterationEventDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["index"] = value.get("index", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> MapIterationEventDetails:
    out: MapIterationEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("index") is not None:
        out["index"] = data["index"]
    else:
        out["index"] = 0
    return out
