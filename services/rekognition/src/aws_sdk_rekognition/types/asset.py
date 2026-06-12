"""Generated from Smithy shape ``com.amazonaws.rekognition#Asset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.ground_truth_manifest


class Asset(TypedDict):
    ground_truth_manifest: NotRequired[
        "aws_sdk_rekognition.types.ground_truth_manifest.GroundTruthManifest"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Asset) -> dict:
    out: dict = {}
    if "ground_truth_manifest" in value:
        import aws_sdk_rekognition.types.ground_truth_manifest

        out["GroundTruthManifest"] = (
            aws_sdk_rekognition.types.ground_truth_manifest.serialize_aws_json_1_1(
                value["ground_truth_manifest"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Asset:
    out: Asset = {}  # type: ignore[typeddict-item]
    if "GroundTruthManifest" in data:
        import aws_sdk_rekognition.types.ground_truth_manifest

        out["ground_truth_manifest"] = (
            aws_sdk_rekognition.types.ground_truth_manifest.deserialize_aws_json_1_1(
                data["GroundTruthManifest"]
            )
        )
    return out
