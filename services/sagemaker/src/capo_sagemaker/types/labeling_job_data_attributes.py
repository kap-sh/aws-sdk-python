"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobDataAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.content_classifiers


class LabelingJobDataAttributes(TypedDict, closed=True):
    content_classifiers: NotRequired[
        "capo_sagemaker.types.content_classifiers.ContentClassifiers"
    ]
    """<p>Declares that your content is free of personally identifiable information or adult content. SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobDataAttributes) -> dict:
    out: dict = {}
    if "content_classifiers" in value:
        import capo_sagemaker.types.content_classifiers

        out["ContentClassifiers"] = (
            capo_sagemaker.types.content_classifiers.serialize_aws_json_1_1(
                value["content_classifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobDataAttributes:
    out: LabelingJobDataAttributes = {}  # type: ignore[typeddict-item]
    if "ContentClassifiers" in data:
        import capo_sagemaker.types.content_classifiers

        out["content_classifiers"] = (
            capo_sagemaker.types.content_classifiers.deserialize_aws_json_1_1(
                data["ContentClassifiers"]
            )
        )
    return out
