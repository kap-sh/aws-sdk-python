"""Generated from Smithy shape ``com.amazonaws.synthetics#ArtifactConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.s3_encryption_config


class ArtifactConfigOutput(TypedDict):
    s3_encryption: NotRequired[
        "aws_sdk_synthetics.types.s3_encryption_config.S3EncryptionConfig"
    ]
    """<p>A structure that contains the configuration of encryption settings for canary artifacts that are stored in Amazon S3. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactConfigOutput) -> dict:
    out: dict = {}
    if "s3_encryption" in value:
        import aws_sdk_synthetics.types.s3_encryption_config

        out["S3Encryption"] = (
            aws_sdk_synthetics.types.s3_encryption_config.serialize_json(
                value["s3_encryption"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArtifactConfigOutput:
    out: ArtifactConfigOutput = {}  # type: ignore[typeddict-item]
    if "S3Encryption" in data:
        import aws_sdk_synthetics.types.s3_encryption_config

        out["s3_encryption"] = (
            aws_sdk_synthetics.types.s3_encryption_config.deserialize_json(
                data["S3Encryption"]
            )
        )
    return out
