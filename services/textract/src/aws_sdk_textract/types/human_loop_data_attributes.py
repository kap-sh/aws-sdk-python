"""Generated from Smithy shape ``com.amazonaws.textract#HumanLoopDataAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.content_classifiers


class HumanLoopDataAttributes(TypedDict):
    content_classifiers: NotRequired[
        "aws_sdk_textract.types.content_classifiers.ContentClassifiers"
    ]
    """<p>Sets whether the input image is free of personally identifiable information or adult content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopDataAttributes) -> dict:
    out: dict = {}
    if "content_classifiers" in value:
        import aws_sdk_textract.types.content_classifiers

        out["ContentClassifiers"] = (
            aws_sdk_textract.types.content_classifiers.serialize_aws_json_1_1(
                value["content_classifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopDataAttributes:
    out: HumanLoopDataAttributes = {}  # type: ignore[typeddict-item]
    if "ContentClassifiers" in data:
        import aws_sdk_textract.types.content_classifiers

        out["content_classifiers"] = (
            aws_sdk_textract.types.content_classifiers.deserialize_aws_json_1_1(
                data["ContentClassifiers"]
            )
        )
    return out
