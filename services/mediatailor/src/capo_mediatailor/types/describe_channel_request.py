"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class DescribeChannelRequest(TypedDict, closed=True):
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelRequest:
    out: DescribeChannelRequest = {}  # type: ignore[typeddict-item]
    return out
