"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.time_in_milli_seconds


class AudioSpecification(TypedDict, closed=True):
    max_length_ms: (
        "aws_sdk_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.</p>"""
    end_timeout_ms: (
        "aws_sdk_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>Time for which a bot waits after the customer stops speaking to assume the utterance is finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSpecification) -> dict:
    out: dict = {}
    out["maxLengthMs"] = value["max_length_ms"]
    out["endTimeoutMs"] = value["end_timeout_ms"]
    return out


def deserialize_json(data: dict) -> AudioSpecification:
    out: AudioSpecification = {}  # type: ignore[typeddict-item]
    if "maxLengthMs" in data:
        out["max_length_ms"] = data["maxLengthMs"]
    else:
        raise DeserializationError("AudioSpecification.max_length_ms required")
    if "endTimeoutMs" in data:
        out["end_timeout_ms"] = data["endTimeoutMs"]
    else:
        raise DeserializationError("AudioSpecification.end_timeout_ms required")
    return out
