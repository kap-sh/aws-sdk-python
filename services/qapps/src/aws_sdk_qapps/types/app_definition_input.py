"""Generated from Smithy shape ``com.amazonaws.qapps#AppDefinitionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_list
    import aws_sdk_qapps.types.initial_prompt


class AppDefinitionInput(TypedDict):
    cards: "aws_sdk_qapps.types.card_list.CardList"
    """<p>The cards that make up the Q App definition.</p>"""
    initial_prompt: NotRequired["aws_sdk_qapps.types.initial_prompt.InitialPrompt"]
    """<p>The initial prompt displayed when the Q App is started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppDefinitionInput) -> dict:
    out: dict = {}
    import aws_sdk_qapps.types.card_list

    out["cards"] = aws_sdk_qapps.types.card_list.serialize_json(value["cards"])
    if "initial_prompt" in value:
        out["initialPrompt"] = value["initial_prompt"]
    return out


def deserialize_json(data: dict) -> AppDefinitionInput:
    out: AppDefinitionInput = {}  # type: ignore[typeddict-item]
    if "cards" in data:
        import aws_sdk_qapps.types.card_list

        out["cards"] = aws_sdk_qapps.types.card_list.deserialize_json(data["cards"])
    else:
        raise DeserializationError("AppDefinitionInput.cards required")
    if "initialPrompt" in data:
        out["initial_prompt"] = data["initialPrompt"]
    return out
