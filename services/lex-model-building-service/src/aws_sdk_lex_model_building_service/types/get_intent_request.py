"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetIntentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_name
    import aws_sdk_lex_model_building_service.types.version


class GetIntentRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent. The name is case sensitive. </p>"""
    version: "aws_sdk_lex_model_building_service.types.version.Version"
    """<p>The version of the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntentRequest:
    out: GetIntentRequest = {}  # type: ignore[typeddict-item]
    return out
