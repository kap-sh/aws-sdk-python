"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteIntentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_name


class DeleteIntentRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent. The name is case sensitive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntentRequest:
    out: DeleteIntentRequest = {}  # type: ignore[typeddict-item]
    return out
