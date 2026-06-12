"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_properties

DocumentClassifierPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.document_classifier_properties.DocumentClassifierProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierPropertiesList) -> list:
    import aws_sdk_comprehend.types.document_classifier_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.document_classifier_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentClassifierPropertiesList:
    import aws_sdk_comprehend.types.document_classifier_properties

    out: DocumentClassifierPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.document_classifier_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
