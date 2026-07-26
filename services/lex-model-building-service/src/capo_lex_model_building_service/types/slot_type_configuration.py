"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.slot_type_regex_configuration


class SlotTypeConfiguration(TypedDict, closed=True):
    regex_configuration: NotRequired[
        "capo_lex_model_building_service.types.slot_type_regex_configuration.SlotTypeRegexConfiguration"
    ]
    """<p>A regular expression used to validate the value of a slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeConfiguration) -> dict:
    out: dict = {}
    if "regex_configuration" in value:
        import capo_lex_model_building_service.types.slot_type_regex_configuration

        out["regexConfiguration"] = (
            capo_lex_model_building_service.types.slot_type_regex_configuration.serialize_json(
                value["regex_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotTypeConfiguration:
    out: SlotTypeConfiguration = {}  # type: ignore[typeddict-item]
    if "regexConfiguration" in data:
        import capo_lex_model_building_service.types.slot_type_regex_configuration

        out["regex_configuration"] = (
            capo_lex_model_building_service.types.slot_type_regex_configuration.deserialize_json(
                data["regexConfiguration"]
            )
        )
    return out
