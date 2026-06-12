"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioAndDTMFInputSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_specification
    import aws_sdk_lex_models_v2.types.dtmf_specification
    import aws_sdk_lex_models_v2.types.time_in_milli_seconds


class AudioAndDTMFInputSpecification(TypedDict):
    start_timeout_ms: (
        "aws_sdk_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>Time for which a bot waits before assuming that the customer isn't going to speak or press a key. This timeout is shared between Audio and DTMF inputs.</p>"""
    audio_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.audio_specification.AudioSpecification"
    ]
    """<p>Specifies the settings on audio input.</p>"""
    dtmf_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.dtmf_specification.DTMFSpecification"
    ]
    """<p>Specifies the settings on DTMF input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioAndDTMFInputSpecification) -> dict:
    out: dict = {}
    out["startTimeoutMs"] = value["start_timeout_ms"]
    if "audio_specification" in value:
        import aws_sdk_lex_models_v2.types.audio_specification

        out["audioSpecification"] = (
            aws_sdk_lex_models_v2.types.audio_specification.serialize_json(
                value["audio_specification"]
            )
        )
    if "dtmf_specification" in value:
        import aws_sdk_lex_models_v2.types.dtmf_specification

        out["dtmfSpecification"] = (
            aws_sdk_lex_models_v2.types.dtmf_specification.serialize_json(
                value["dtmf_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioAndDTMFInputSpecification:
    out: AudioAndDTMFInputSpecification = {}  # type: ignore[typeddict-item]
    if "startTimeoutMs" in data:
        out["start_timeout_ms"] = data["startTimeoutMs"]
    else:
        raise DeserializationError(
            "AudioAndDTMFInputSpecification.start_timeout_ms required"
        )
    if "audioSpecification" in data:
        import aws_sdk_lex_models_v2.types.audio_specification

        out["audio_specification"] = (
            aws_sdk_lex_models_v2.types.audio_specification.deserialize_json(
                data["audioSpecification"]
            )
        )
    if "dtmfSpecification" in data:
        import aws_sdk_lex_models_v2.types.dtmf_specification

        out["dtmf_specification"] = (
            aws_sdk_lex_models_v2.types.dtmf_specification.deserialize_json(
                data["dtmfSpecification"]
            )
        )
    return out
