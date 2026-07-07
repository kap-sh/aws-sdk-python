"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetChanges``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.ground_truth_blob


class DatasetChanges(TypedDict, closed=True):
    ground_truth: "aws_sdk_rekognition.types.ground_truth_blob.GroundTruthBlob"
    """<p>A Base64-encoded binary data object containing one or JSON lines that either update the dataset or are additions to the dataset. You change a dataset by calling <a>UpdateDatasetEntries</a>. If you are using an AWS SDK to call <code>UpdateDatasetEntries</code>, you don't need to encode <code>Changes</code> as the SDK encodes the data for you. </p> <p>For example JSON lines, see Image-Level labels in manifest files and and Object localization in manifest files in the <i>Amazon Rekognition Custom Labels Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetChanges) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.ground_truth_blob

    out["GroundTruth"] = (
        aws_sdk_rekognition.types.ground_truth_blob.serialize_aws_json_1_1(
            value["ground_truth"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetChanges:
    out: DatasetChanges = {}  # type: ignore[typeddict-item]
    if "GroundTruth" in data:
        import aws_sdk_rekognition.types.ground_truth_blob

        out["ground_truth"] = (
            aws_sdk_rekognition.types.ground_truth_blob.deserialize_aws_json_1_1(
                data["GroundTruth"]
            )
        )
    else:
        raise DeserializationError("DatasetChanges.ground_truth required")
    return out
