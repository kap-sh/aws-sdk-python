"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopDataAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.content_classifiers


class HumanLoopDataAttributes(TypedDict, closed=True):
    content_classifiers: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.content_classifiers.ContentClassifiers"
    ]
    """<p>Declares that your content is free of personally identifiable information or adult content.</p> <p>Amazon SageMaker can restrict the Amazon Mechanical Turk workers who can view your task based on this information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanLoopDataAttributes) -> dict:
    out: dict = {}
    if "content_classifiers" in value:
        import aws_sdk_sagemaker_a2i_runtime.types.content_classifiers

        out["ContentClassifiers"] = (
            aws_sdk_sagemaker_a2i_runtime.types.content_classifiers.serialize_json(
                value["content_classifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> HumanLoopDataAttributes:
    out: HumanLoopDataAttributes = {}  # type: ignore[typeddict-item]
    if "ContentClassifiers" in data:
        import aws_sdk_sagemaker_a2i_runtime.types.content_classifiers

        out["content_classifiers"] = (
            aws_sdk_sagemaker_a2i_runtime.types.content_classifiers.deserialize_json(
                data["ContentClassifiers"]
            )
        )
    return out
