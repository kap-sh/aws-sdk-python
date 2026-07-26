"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.response_mode


class ParticipantConfiguration(TypedDict, closed=True):
    response_mode: NotRequired["capo_connect.types.response_mode.ResponseMode"]
    """<p> The mode in which responses should be sent to the participant. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantConfiguration) -> dict:
    out: dict = {}
    if "response_mode" in value:
        import capo_connect.types.response_mode

        out["ResponseMode"] = capo_connect.types.response_mode.serialize_json(
            value["response_mode"]
        )
    return out


def deserialize_json(data: dict) -> ParticipantConfiguration:
    out: ParticipantConfiguration = {}  # type: ignore[typeddict-item]
    if "ResponseMode" in data:
        import capo_connect.types.response_mode

        out["response_mode"] = capo_connect.types.response_mode.deserialize_json(
            data["ResponseMode"]
        )
    return out
