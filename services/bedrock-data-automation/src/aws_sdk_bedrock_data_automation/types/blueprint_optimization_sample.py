"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationSample``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.s3_object


class BlueprintOptimizationSample(TypedDict, closed=True):
    asset_s3_object: "aws_sdk_bedrock_data_automation.types.s3_object.S3Object"
    """S3 Object of the asset"""
    ground_truth_s3_object: "aws_sdk_bedrock_data_automation.types.s3_object.S3Object"
    """Ground truth for the Blueprint and Asset combination"""


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintOptimizationSample) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.s3_object

    out["assetS3Object"] = (
        aws_sdk_bedrock_data_automation.types.s3_object.serialize_json(
            value["asset_s3_object"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.s3_object

    out["groundTruthS3Object"] = (
        aws_sdk_bedrock_data_automation.types.s3_object.serialize_json(
            value["ground_truth_s3_object"]
        )
    )
    return out


def deserialize_json(data: dict) -> BlueprintOptimizationSample:
    out: BlueprintOptimizationSample = {}  # type: ignore[typeddict-item]
    if "assetS3Object" in data:
        import aws_sdk_bedrock_data_automation.types.s3_object

        out["asset_s3_object"] = (
            aws_sdk_bedrock_data_automation.types.s3_object.deserialize_json(
                data["assetS3Object"]
            )
        )
    else:
        raise DeserializationError(
            "BlueprintOptimizationSample.asset_s3_object required"
        )
    if "groundTruthS3Object" in data:
        import aws_sdk_bedrock_data_automation.types.s3_object

        out["ground_truth_s3_object"] = (
            aws_sdk_bedrock_data_automation.types.s3_object.deserialize_json(
                data["groundTruthS3Object"]
            )
        )
    else:
        raise DeserializationError(
            "BlueprintOptimizationSample.ground_truth_s3_object required"
        )
    return out
