"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DTMFSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.dtmf_character
    import aws_sdk_lex_models_v2.types.max_utterance_digits
    import aws_sdk_lex_models_v2.types.time_in_milli_seconds


class DTMFSpecification(TypedDict):
    max_length: "aws_sdk_lex_models_v2.types.max_utterance_digits.MaxUtteranceDigits"
    """<p>The maximum number of DTMF digits allowed in an utterance.</p>"""
    end_timeout_ms: (
        "aws_sdk_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>How long the bot should wait after the last DTMF character input before assuming that the input has concluded.</p>"""
    deletion_character: "aws_sdk_lex_models_v2.types.dtmf_character.DTMFCharacter"
    """<p>The DTMF character that clears the accumulated DTMF digits and immediately ends the input.</p>"""
    end_character: "aws_sdk_lex_models_v2.types.dtmf_character.DTMFCharacter"
    """<p>The DTMF character that immediately ends input. If the user does not press this character, the input ends after the end timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DTMFSpecification) -> dict:
    out: dict = {}
    out["maxLength"] = value["max_length"]
    out["endTimeoutMs"] = value["end_timeout_ms"]
    out["deletionCharacter"] = value["deletion_character"]
    out["endCharacter"] = value["end_character"]
    return out


def deserialize_json(data: dict) -> DTMFSpecification:
    out: DTMFSpecification = {}  # type: ignore[typeddict-item]
    if "maxLength" in data:
        out["max_length"] = data["maxLength"]
    else:
        raise DeserializationError("DTMFSpecification.max_length required")
    if "endTimeoutMs" in data:
        out["end_timeout_ms"] = data["endTimeoutMs"]
    else:
        raise DeserializationError("DTMFSpecification.end_timeout_ms required")
    if "deletionCharacter" in data:
        out["deletion_character"] = data["deletionCharacter"]
    else:
        raise DeserializationError("DTMFSpecification.deletion_character required")
    if "endCharacter" in data:
        out["end_character"] = data["endCharacter"]
    else:
        raise DeserializationError("DTMFSpecification.end_character required")
    return out
