"""Generated from Smithy shape ``com.amazonaws.rekognition#TrainingDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.training_data
    import aws_sdk_rekognition.types.validation_data


class TrainingDataResult(TypedDict, closed=True):
    input: NotRequired["aws_sdk_rekognition.types.training_data.TrainingData"]
    """<p>The training data that you supplied.</p>"""
    output: NotRequired["aws_sdk_rekognition.types.training_data.TrainingData"]
    """<p>Reference to images (assets) that were actually used during training with trained model predictions.</p>"""
    validation: NotRequired["aws_sdk_rekognition.types.validation_data.ValidationData"]
    """<p>A manifest that you supplied for training, with validation results for each line.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingDataResult) -> dict:
    out: dict = {}
    if "input" in value:
        import aws_sdk_rekognition.types.training_data

        out["Input"] = aws_sdk_rekognition.types.training_data.serialize_aws_json_1_1(
            value["input"]
        )
    if "output" in value:
        import aws_sdk_rekognition.types.training_data

        out["Output"] = aws_sdk_rekognition.types.training_data.serialize_aws_json_1_1(
            value["output"]
        )
    if "validation" in value:
        import aws_sdk_rekognition.types.validation_data

        out["Validation"] = (
            aws_sdk_rekognition.types.validation_data.serialize_aws_json_1_1(
                value["validation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingDataResult:
    out: TrainingDataResult = {}  # type: ignore[typeddict-item]
    if "Input" in data:
        import aws_sdk_rekognition.types.training_data

        out["input"] = aws_sdk_rekognition.types.training_data.deserialize_aws_json_1_1(
            data["Input"]
        )
    if "Output" in data:
        import aws_sdk_rekognition.types.training_data

        out["output"] = (
            aws_sdk_rekognition.types.training_data.deserialize_aws_json_1_1(
                data["Output"]
            )
        )
    if "Validation" in data:
        import aws_sdk_rekognition.types.validation_data

        out["validation"] = (
            aws_sdk_rekognition.types.validation_data.deserialize_aws_json_1_1(
                data["Validation"]
            )
        )
    return out
