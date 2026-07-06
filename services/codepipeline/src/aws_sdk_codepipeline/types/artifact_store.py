"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_store_location
    import aws_sdk_codepipeline.types.artifact_store_type
    import aws_sdk_codepipeline.types.encryption_key


class ArtifactStore(TypedDict, closed=True):
    type: "aws_sdk_codepipeline.types.artifact_store_type.ArtifactStoreType"
    """<p>The type of the artifact store, such as S3.</p>"""
    location: "aws_sdk_codepipeline.types.artifact_store_location.ArtifactStoreLocation"
    """<p>The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same Amazon Web Services Region as the pipeline to store your pipeline artifacts.</p>"""
    encryption_key: NotRequired[
        "aws_sdk_codepipeline.types.encryption_key.EncryptionKey"
    ]
    """<p>The encryption key used to encrypt the data in the artifact store, such as an Amazon Web Services Key Management Service key. If this is undefined, the default key for Amazon S3 is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactStore) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.artifact_store_type

    out["type"] = aws_sdk_codepipeline.types.artifact_store_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["location"] = value["location"]
    if "encryption_key" in value:
        import aws_sdk_codepipeline.types.encryption_key

        out["encryptionKey"] = (
            aws_sdk_codepipeline.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactStore:
    out: ArtifactStore = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_codepipeline.types.artifact_store_type

        out["type"] = (
            aws_sdk_codepipeline.types.artifact_store_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ArtifactStore.type required")
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("ArtifactStore.location required")
    if "encryptionKey" in data:
        import aws_sdk_codepipeline.types.encryption_key

        out["encryption_key"] = (
            aws_sdk_codepipeline.types.encryption_key.deserialize_aws_json_1_1(
                data["encryptionKey"]
            )
        )
    return out
