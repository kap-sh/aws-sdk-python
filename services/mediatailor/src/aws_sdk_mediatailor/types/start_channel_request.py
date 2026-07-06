"""Generated from Smithy shape ``com.amazonaws.mediatailor#StartChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class StartChannelRequest(TypedDict, closed=True):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartChannelRequest:
    out: StartChannelRequest = {}  # type: ignore[typeddict-item]
    return out
