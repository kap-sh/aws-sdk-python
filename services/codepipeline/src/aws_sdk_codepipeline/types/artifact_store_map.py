"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactStoreMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_store
    import aws_sdk_codepipeline.types.aws_region_name

ArtifactStoreMap: TypeAlias = dict[
    "aws_sdk_codepipeline.types.aws_region_name.AWSRegionName",
    "aws_sdk_codepipeline.types.artifact_store.ArtifactStore",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ArtifactStoreMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_codepipeline.types.artifact_store

        out[key] = aws_sdk_codepipeline.types.artifact_store.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactStoreMap:
    out: ArtifactStoreMap = {}
    for key, value in data.items():
        import aws_sdk_codepipeline.types.artifact_store

        out[key] = aws_sdk_codepipeline.types.artifact_store.deserialize_aws_json_1_1(
            value
        )
    return out
