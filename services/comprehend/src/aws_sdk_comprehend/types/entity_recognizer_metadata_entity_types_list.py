"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerMetadataEntityTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list_item

EntityRecognizerMetadataEntityTypesList: TypeAlias = list[
    "aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list_item.EntityRecognizerMetadataEntityTypesListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerMetadataEntityTypesList) -> list:
    import aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityRecognizerMetadataEntityTypesList:
    import aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list_item

    out: EntityRecognizerMetadataEntityTypesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
