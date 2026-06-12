"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TextInputSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.time_in_milli_seconds


class TextInputSpecification(TypedDict):
    start_timeout_ms: (
        "aws_sdk_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>Time for which a bot waits before re-prompting a customer for text input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputSpecification) -> dict:
    out: dict = {}
    out["startTimeoutMs"] = value["start_timeout_ms"]
    return out


def deserialize_json(data: dict) -> TextInputSpecification:
    out: TextInputSpecification = {}  # type: ignore[typeddict-item]
    if "startTimeoutMs" in data:
        out["start_timeout_ms"] = data["startTimeoutMs"]
    else:
        raise DeserializationError("TextInputSpecification.start_timeout_ms required")
    return out
