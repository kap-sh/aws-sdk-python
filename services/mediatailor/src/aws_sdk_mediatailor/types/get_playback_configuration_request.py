"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetPlaybackConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class GetPlaybackConfigurationRequest(TypedDict):
    name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The identifier for the playback configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaybackConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPlaybackConfigurationRequest:
    out: GetPlaybackConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
