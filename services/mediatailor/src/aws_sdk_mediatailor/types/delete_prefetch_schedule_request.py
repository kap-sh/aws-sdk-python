"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeletePrefetchScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeletePrefetchScheduleRequest(TypedDict, closed=True):
    name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.</p>"""
    playback_configuration_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the playback configuration for this prefetch schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrefetchScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePrefetchScheduleRequest:
    out: DeletePrefetchScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
