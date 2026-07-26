"""Generated from Smithy shape ``com.amazonaws.glue#EnclosedInStringPropertiesMinOne``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property

EnclosedInStringPropertiesMinOne: TypeAlias = list[
    "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnclosedInStringPropertiesMinOne) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EnclosedInStringPropertiesMinOne:
    return list(data)
