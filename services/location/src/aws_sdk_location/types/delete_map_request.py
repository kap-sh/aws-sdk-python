"""Generated from Smithy shape ``com.amazonaws.location#DeleteMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name


class DeleteMapRequest(TypedDict, closed=True):
    map_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the map resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMapRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMapRequest:
    out: DeleteMapRequest = {}  # type: ignore[typeddict-item]
    return out
