"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#ContentClassifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.content_classifier

ContentClassifiers: TypeAlias = list[
    "aws_sdk_sagemaker_a2i_runtime.types.content_classifier.ContentClassifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentClassifiers) -> list:
    import aws_sdk_sagemaker_a2i_runtime.types.content_classifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker_a2i_runtime.types.content_classifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContentClassifiers:
    import aws_sdk_sagemaker_a2i_runtime.types.content_classifier

    out: ContentClassifiers = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_a2i_runtime.types.content_classifier.deserialize_json(
                item
            )
        )
    return out
