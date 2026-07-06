"""Generated from Smithy shape ``com.amazonaws.location#DeleteTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name


class DeleteTrackerRequest(TypedDict, closed=True):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrackerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrackerRequest:
    out: DeleteTrackerRequest = {}  # type: ignore[typeddict-item]
    return out
