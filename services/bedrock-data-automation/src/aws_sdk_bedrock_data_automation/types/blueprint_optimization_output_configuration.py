"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.s3_object


class BlueprintOptimizationOutputConfiguration(TypedDict):
    s3_object: "aws_sdk_bedrock_data_automation.types.s3_object.S3Object"
    """S3 object."""


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintOptimizationOutputConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.s3_object

    out["s3Object"] = aws_sdk_bedrock_data_automation.types.s3_object.serialize_json(
        value["s3_object"]
    )
    return out


def deserialize_json(data: dict) -> BlueprintOptimizationOutputConfiguration:
    out: BlueprintOptimizationOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Object" in data:
        import aws_sdk_bedrock_data_automation.types.s3_object

        out["s3_object"] = (
            aws_sdk_bedrock_data_automation.types.s3_object.deserialize_json(
                data["s3Object"]
            )
        )
    else:
        raise DeserializationError(
            "BlueprintOptimizationOutputConfiguration.s3_object required"
        )
    return out
