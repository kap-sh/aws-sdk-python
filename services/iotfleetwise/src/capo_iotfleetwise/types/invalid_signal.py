"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fully_qualified_name
    import capo_iotfleetwise.types.string


class InvalidSignal(TypedDict, closed=True):
    name: NotRequired["capo_iotfleetwise.types.fully_qualified_name.FullyQualifiedName"]
    """<p>The name of the signal that isn't valid.</p>"""
    reason: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>A message about why the signal isn't valid.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidSignal) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidSignal:
    out: InvalidSignal = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
