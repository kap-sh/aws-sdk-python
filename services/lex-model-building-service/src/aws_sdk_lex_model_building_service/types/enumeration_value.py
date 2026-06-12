"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#EnumerationValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.synonym_list
    import aws_sdk_lex_model_building_service.types.value


class EnumerationValue(TypedDict):
    value: "aws_sdk_lex_model_building_service.types.value.Value"
    """<p>The value of the slot type.</p>"""
    synonyms: NotRequired[
        "aws_sdk_lex_model_building_service.types.synonym_list.SynonymList"
    ]
    """<p>Additional values related to the slot type value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnumerationValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "synonyms" in value:
        import aws_sdk_lex_model_building_service.types.synonym_list

        out["synonyms"] = (
            aws_sdk_lex_model_building_service.types.synonym_list.serialize_json(
                value["synonyms"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnumerationValue:
    out: EnumerationValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnumerationValue.value required")
    if "synonyms" in data:
        import aws_sdk_lex_model_building_service.types.synonym_list

        out["synonyms"] = (
            aws_sdk_lex_model_building_service.types.synonym_list.deserialize_json(
                data["synonyms"]
            )
        )
    return out
