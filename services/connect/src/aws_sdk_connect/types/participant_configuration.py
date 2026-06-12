"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.response_mode


class ParticipantConfiguration(TypedDict):
    response_mode: NotRequired["aws_sdk_connect.types.response_mode.ResponseMode"]
    """<p> The mode in which responses should be sent to the participant. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantConfiguration) -> dict:
    out: dict = {}
    if "response_mode" in value:
        import aws_sdk_connect.types.response_mode

        out["ResponseMode"] = aws_sdk_connect.types.response_mode.serialize_json(
            value["response_mode"]
        )
    return out


def deserialize_json(data: dict) -> ParticipantConfiguration:
    out: ParticipantConfiguration = {}  # type: ignore[typeddict-item]
    if "ResponseMode" in data:
        import aws_sdk_connect.types.response_mode

        out["response_mode"] = aws_sdk_connect.types.response_mode.deserialize_json(
            data["ResponseMode"]
        )
    return out
