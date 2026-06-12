"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetChannelPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class GetChannelPolicyRequest(TypedDict):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel associated with this Channel Policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelPolicyRequest:
    out: GetChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
