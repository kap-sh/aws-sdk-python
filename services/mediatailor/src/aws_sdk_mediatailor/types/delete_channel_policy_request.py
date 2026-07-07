"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteChannelPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteChannelPolicyRequest(TypedDict, closed=True):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel associated with this channel policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelPolicyRequest:
    out: DeleteChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
