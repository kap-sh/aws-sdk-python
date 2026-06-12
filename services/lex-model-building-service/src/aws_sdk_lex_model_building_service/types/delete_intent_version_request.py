"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteIntentVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_name
    import aws_sdk_lex_model_building_service.types.numerical_version


class DeleteIntentVersionRequest(TypedDict):
    name: "aws_sdk_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent.</p>"""
    version: (
        "aws_sdk_lex_model_building_service.types.numerical_version.NumericalVersion"
    )
    """<p>The version of the intent to delete. You cannot delete the <code>$LATEST</code> version of the intent. To delete the <code>$LATEST</code> version, use the <a>DeleteIntent</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntentVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntentVersionRequest:
    out: DeleteIntentVersionRequest = {}  # type: ignore[typeddict-item]
    return out
