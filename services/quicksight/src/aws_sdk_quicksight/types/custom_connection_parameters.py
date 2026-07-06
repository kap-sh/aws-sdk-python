"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomConnectionParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class CustomConnectionParameters(TypedDict, closed=True):
    connection_type: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The type of custom connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectionParameters) -> dict:
    out: dict = {}
    if "connection_type" in value:
        out["ConnectionType"] = value["connection_type"]
    return out


def deserialize_json(data: dict) -> CustomConnectionParameters:
    out: CustomConnectionParameters = {}  # type: ignore[typeddict-item]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    return out
