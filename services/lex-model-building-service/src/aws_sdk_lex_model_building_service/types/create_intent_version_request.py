"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CreateIntentVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_name
    import aws_sdk_lex_model_building_service.types.string


class CreateIntentVersionRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent that you want to create a new version of. The name is case sensitive. </p>"""
    checksum: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>Checksum of the <code>$LATEST</code> version of the intent that should be used to create the new version. If you specify a checksum and the <code>$LATEST</code> version of the intent has a different checksum, Amazon Lex returns a <code>PreconditionFailedException</code> exception and doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the <code>$LATEST</code> version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntentVersionRequest) -> dict:
    out: dict = {}
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    return out


def deserialize_json(data: dict) -> CreateIntentVersionRequest:
    out: CreateIntentVersionRequest = {}  # type: ignore[typeddict-item]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    return out
