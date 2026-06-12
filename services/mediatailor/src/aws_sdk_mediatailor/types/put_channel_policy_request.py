"""Generated from Smithy shape ``com.amazonaws.mediatailor#PutChannelPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class PutChannelPolicyRequest(TypedDict):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The channel name associated with this Channel Policy.</p>"""
    policy: "aws_sdk_mediatailor.types.__string.__string"
    """<p>Adds an IAM role that determines the permissions of your channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutChannelPolicyRequest:
    out: PutChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutChannelPolicyRequest.policy required")
    return out
