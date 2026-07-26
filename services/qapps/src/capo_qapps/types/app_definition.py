"""Generated from Smithy shape ``com.amazonaws.qapps#AppDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.card_model_list


class AppDefinition(TypedDict, closed=True):
    app_definition_version: "str"
    """<p>The version of the app definition schema or specification.</p>"""
    cards: "capo_qapps.types.card_model_list.CardModelList"
    """<p>The cards that make up the Q App, such as text input, file upload, or query cards.</p>"""
    can_edit: NotRequired["bool"]
    """<p>A flag indicating whether the Q App's definition can be edited by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppDefinition) -> dict:
    out: dict = {}
    out["appDefinitionVersion"] = value["app_definition_version"]
    import capo_qapps.types.card_model_list

    out["cards"] = capo_qapps.types.card_model_list.serialize_json(value["cards"])
    if "can_edit" in value:
        out["canEdit"] = value["can_edit"]
    return out


def deserialize_json(data: dict) -> AppDefinition:
    out: AppDefinition = {}  # type: ignore[typeddict-item]
    if "appDefinitionVersion" in data:
        out["app_definition_version"] = data["appDefinitionVersion"]
    else:
        raise DeserializationError("AppDefinition.app_definition_version required")
    if "cards" in data:
        import capo_qapps.types.card_model_list

        out["cards"] = capo_qapps.types.card_model_list.deserialize_json(data["cards"])
    else:
        raise DeserializationError("AppDefinition.cards required")
    if "canEdit" in data:
        out["can_edit"] = data["canEdit"]
    return out
