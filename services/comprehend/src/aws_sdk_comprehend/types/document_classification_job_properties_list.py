"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassificationJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classification_job_properties

DocumentClassificationJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.document_classification_job_properties.DocumentClassificationJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassificationJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.document_classification_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.document_classification_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentClassificationJobPropertiesList:
    import aws_sdk_comprehend.types.document_classification_job_properties

    out: DocumentClassificationJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.document_classification_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
