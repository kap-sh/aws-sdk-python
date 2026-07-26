"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_properties

EntityRecognizerPropertiesList: TypeAlias = list[
    "capo_comprehend.types.entity_recognizer_properties.EntityRecognizerProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerPropertiesList) -> list:
    import capo_comprehend.types.entity_recognizer_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.entity_recognizer_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityRecognizerPropertiesList:
    import capo_comprehend.types.entity_recognizer_properties

    out: EntityRecognizerPropertiesList = []
    for item in data:
        out.append(
            capo_comprehend.types.entity_recognizer_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
