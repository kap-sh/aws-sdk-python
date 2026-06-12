"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDocumentReadFeatureTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_read_feature_types

ListOfDocumentReadFeatureTypes: TypeAlias = list[
    "aws_sdk_comprehend.types.document_read_feature_types.DocumentReadFeatureTypes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDocumentReadFeatureTypes) -> list:
    import aws_sdk_comprehend.types.document_read_feature_types

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.document_read_feature_types.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDocumentReadFeatureTypes:
    import aws_sdk_comprehend.types.document_read_feature_types

    out: ListOfDocumentReadFeatureTypes = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.document_read_feature_types.deserialize_aws_json_1_1(
                item
            )
        )
    return out
