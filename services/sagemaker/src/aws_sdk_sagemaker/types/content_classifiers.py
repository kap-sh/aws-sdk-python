"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContentClassifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.content_classifier

ContentClassifiers: TypeAlias = list[
    "aws_sdk_sagemaker.types.content_classifier.ContentClassifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentClassifiers) -> list:
    import aws_sdk_sagemaker.types.content_classifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.content_classifier.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContentClassifiers:
    import aws_sdk_sagemaker.types.content_classifier

    out: ContentClassifiers = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.content_classifier.deserialize_aws_json_1_1(item)
        )
    return out
