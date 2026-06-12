"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#EnumerationValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.enumeration_value

EnumerationValues: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.enumeration_value.EnumerationValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnumerationValues) -> list:
    import aws_sdk_lex_model_building_service.types.enumeration_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.enumeration_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnumerationValues:
    import aws_sdk_lex_model_building_service.types.enumeration_value

    out: EnumerationValues = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.enumeration_value.deserialize_json(
                item
            )
        )
    return out
