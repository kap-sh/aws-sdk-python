"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Intent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_name
    import aws_sdk_lex_model_building_service.types.version


class Intent(TypedDict, closed=True):
    intent_name: "aws_sdk_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent.</p>"""
    intent_version: "aws_sdk_lex_model_building_service.types.version.Version"
    """<p>The version of the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Intent) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["intentVersion"] = value["intent_version"]
    return out


def deserialize_json(data: dict) -> Intent:
    out: Intent = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    else:
        raise DeserializationError("Intent.intent_name required")
    if "intentVersion" in data:
        out["intent_version"] = data["intentVersion"]
    else:
        raise DeserializationError("Intent.intent_version required")
    return out
