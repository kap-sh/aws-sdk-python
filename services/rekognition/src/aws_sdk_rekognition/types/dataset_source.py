"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_arn
    import aws_sdk_rekognition.types.ground_truth_manifest


class DatasetSource(TypedDict, closed=True):
    ground_truth_manifest: NotRequired[
        "aws_sdk_rekognition.types.ground_truth_manifest.GroundTruthManifest"
    ]
    dataset_arn: NotRequired["aws_sdk_rekognition.types.dataset_arn.DatasetArn"]
    """<p> The ARN of an Amazon Rekognition Custom Labels dataset that you want to copy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetSource) -> dict:
    out: dict = {}
    if "ground_truth_manifest" in value:
        import aws_sdk_rekognition.types.ground_truth_manifest

        out["GroundTruthManifest"] = (
            aws_sdk_rekognition.types.ground_truth_manifest.serialize_aws_json_1_1(
                value["ground_truth_manifest"]
            )
        )
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetSource:
    out: DatasetSource = {}  # type: ignore[typeddict-item]
    if "GroundTruthManifest" in data:
        import aws_sdk_rekognition.types.ground_truth_manifest

        out["ground_truth_manifest"] = (
            aws_sdk_rekognition.types.ground_truth_manifest.deserialize_aws_json_1_1(
                data["GroundTruthManifest"]
            )
        )
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    return out
