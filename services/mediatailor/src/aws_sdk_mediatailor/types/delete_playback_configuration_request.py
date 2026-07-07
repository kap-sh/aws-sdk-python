"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeletePlaybackConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeletePlaybackConfigurationRequest(TypedDict, closed=True):
    name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the playback configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePlaybackConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePlaybackConfigurationRequest:
    out: DeletePlaybackConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
