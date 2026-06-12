"""Generated from Smithy shape ``com.amazonaws.connect#PostAcceptTimeoutConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.post_accept_preview_timeout_duration_in_seconds


class PostAcceptTimeoutConfig(TypedDict):
    duration_in_seconds: "aws_sdk_connect.types.post_accept_preview_timeout_duration_in_seconds.PostAcceptPreviewTimeoutDurationInSeconds"
    """<p>Duration in seconds for the countdown timer after the agent accepted the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostAcceptTimeoutConfig) -> dict:
    out: dict = {}
    out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> PostAcceptTimeoutConfig:
    out: PostAcceptTimeoutConfig = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "PostAcceptTimeoutConfig.duration_in_seconds required"
        )
    return out
