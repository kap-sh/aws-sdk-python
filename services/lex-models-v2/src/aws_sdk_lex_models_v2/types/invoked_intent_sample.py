"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InvokedIntentSample``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.name


class InvokedIntentSample(TypedDict, closed=True):
    intent_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of an intent that was invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokedIntentSample) -> dict:
    out: dict = {}
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    return out


def deserialize_json(data: dict) -> InvokedIntentSample:
    out: InvokedIntentSample = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    return out
