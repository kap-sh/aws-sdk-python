"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechDetectionSensitivity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>Determines the sensitivity level for voice activity detection (VAD) in noisy environments. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise.</p> <p>Valid values include:</p> <ul> <li> <p> <code>Default</code> - Standard sensitivity level suitable for most environments</p> </li> <li> <p> <code>HighNoiseTolerance</code> - Increased tolerance for moderate background noise</p> </li> <li> <p> <code>MaximumNoiseTolerance</code> - Maximum tolerance for high levels of background noise</p> </li> </ul>"""
SpeechDetectionSensitivity: TypeAlias = Literal[
    "Default",
    "HighNoiseTolerance",
    "MaximumNoiseTolerance",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Default",
        "HighNoiseTolerance",
        "MaximumNoiseTolerance",
    )
)


def serialize_json(value: SpeechDetectionSensitivity) -> str:
    return value


def deserialize_json(data: str) -> SpeechDetectionSensitivity:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SpeechDetectionSensitivity value: {data!r}"
        )
    return cast(SpeechDetectionSensitivity, data)
