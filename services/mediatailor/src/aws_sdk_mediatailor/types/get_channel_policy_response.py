"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetChannelPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class GetChannelPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The IAM policy for the channel. IAM policies are used to control access to your channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetChannelPolicyResponse:
    out: GetChannelPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
