"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorTerminationHealthResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.termination_health


class GetVoiceConnectorTerminationHealthResponse(TypedDict, closed=True):
    termination_health: NotRequired[
        "aws_sdk_chime_sdk_voice.types.termination_health.TerminationHealth"
    ]
    """<p>The termination health details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorTerminationHealthResponse) -> dict:
    out: dict = {}
    if "termination_health" in value:
        import aws_sdk_chime_sdk_voice.types.termination_health

        out["TerminationHealth"] = (
            aws_sdk_chime_sdk_voice.types.termination_health.serialize_json(
                value["termination_health"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorTerminationHealthResponse:
    out: GetVoiceConnectorTerminationHealthResponse = {}  # type: ignore[typeddict-item]
    if "TerminationHealth" in data:
        import aws_sdk_chime_sdk_voice.types.termination_health

        out["termination_health"] = (
            aws_sdk_chime_sdk_voice.types.termination_health.deserialize_json(
                data["TerminationHealth"]
            )
        )
    return out
