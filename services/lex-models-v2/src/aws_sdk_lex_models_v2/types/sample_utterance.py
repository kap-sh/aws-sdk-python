"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SampleUtterance``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.utterance


class SampleUtterance(TypedDict):
    utterance: "aws_sdk_lex_models_v2.types.utterance.Utterance"
    """<p>The sample utterance that Amazon Lex uses to build its machine-learning model to recognize intents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleUtterance) -> dict:
    out: dict = {}
    out["utterance"] = value["utterance"]
    return out


def deserialize_json(data: dict) -> SampleUtterance:
    out: SampleUtterance = {}  # type: ignore[typeddict-item]
    if "utterance" in data:
        out["utterance"] = data["utterance"]
    else:
        raise DeserializationError("SampleUtterance.utterance required")
    return out
