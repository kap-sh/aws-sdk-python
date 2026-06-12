"""Generated from Smithy shape ``com.amazonaws.pi#FeatureMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.feature_metadata
    import aws_sdk_pi.types.string

FeatureMetadataMap: TypeAlias = dict[
    "aws_sdk_pi.types.string.String",
    "aws_sdk_pi.types.feature_metadata.FeatureMetadata",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FeatureMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pi.types.feature_metadata

        out[key] = aws_sdk_pi.types.feature_metadata.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureMetadataMap:
    out: FeatureMetadataMap = {}
    for key, value in data.items():
        import aws_sdk_pi.types.feature_metadata

        out[key] = aws_sdk_pi.types.feature_metadata.deserialize_aws_json_1_1(value)
    return out
