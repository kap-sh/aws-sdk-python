"""Generated from Smithy shape ``com.amazonaws.qbusiness#StringAttributeValueBoosting``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.string
    import capo_qbusiness.types.string_attribute_value_boosting_level

StringAttributeValueBoosting: TypeAlias = dict[
    "capo_qbusiness.types.string.String",
    "capo_qbusiness.types.string_attribute_value_boosting_level.StringAttributeValueBoostingLevel",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StringAttributeValueBoosting) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_qbusiness.types.string_attribute_value_boosting_level

        out[key] = (
            capo_qbusiness.types.string_attribute_value_boosting_level.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> StringAttributeValueBoosting:
    out: StringAttributeValueBoosting = {}
    for key, value in data.items():
        import capo_qbusiness.types.string_attribute_value_boosting_level

        out[key] = (
            capo_qbusiness.types.string_attribute_value_boosting_level.deserialize_json(
                value
            )
        )
    return out
