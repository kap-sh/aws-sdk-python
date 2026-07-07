"""Generated from Smithy shape ``com.amazonaws.rekognition#TrainingData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.assets


class TrainingData(TypedDict, closed=True):
    assets: NotRequired["aws_sdk_rekognition.types.assets.Assets"]
    """<p>A manifest file that contains references to the training images and ground-truth annotations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingData) -> dict:
    out: dict = {}
    if "assets" in value:
        import aws_sdk_rekognition.types.assets

        out["Assets"] = aws_sdk_rekognition.types.assets.serialize_aws_json_1_1(
            value["assets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingData:
    out: TrainingData = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import aws_sdk_rekognition.types.assets

        out["assets"] = aws_sdk_rekognition.types.assets.deserialize_aws_json_1_1(
            data["Assets"]
        )
    return out
