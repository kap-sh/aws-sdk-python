"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotTypeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.slot_type_configuration

SlotTypeConfigurations: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.slot_type_configuration.SlotTypeConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeConfigurations) -> list:
    import aws_sdk_lex_model_building_service.types.slot_type_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.slot_type_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SlotTypeConfigurations:
    import aws_sdk_lex_model_building_service.types.slot_type_configuration

    out: SlotTypeConfigurations = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.slot_type_configuration.deserialize_json(
                item
            )
        )
    return out
