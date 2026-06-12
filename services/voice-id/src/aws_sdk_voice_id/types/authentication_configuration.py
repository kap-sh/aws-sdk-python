"""Generated from Smithy shape ``com.amazonaws.voiceid#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.score


class AuthenticationConfiguration(TypedDict):
    acceptance_threshold: "aws_sdk_voice_id.types.score.Score"
    """<p>The minimum threshold needed to successfully authenticate a speaker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    out["AcceptanceThreshold"] = value["acceptance_threshold"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "AcceptanceThreshold" in data:
        out["acceptance_threshold"] = data["AcceptanceThreshold"]
    else:
        raise DeserializationError(
            "AuthenticationConfiguration.acceptance_threshold required"
        )
    return out
