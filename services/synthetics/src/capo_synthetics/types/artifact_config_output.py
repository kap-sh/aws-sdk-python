"""Generated from Smithy shape ``com.amazonaws.synthetics#ArtifactConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.s3_encryption_config


class ArtifactConfigOutput(TypedDict, closed=True):
    s3_encryption: NotRequired[
        "capo_synthetics.types.s3_encryption_config.S3EncryptionConfig"
    ]
    """<p>A structure that contains the configuration of encryption settings for canary artifacts that are stored in Amazon S3. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactConfigOutput) -> dict:
    out: dict = {}
    if "s3_encryption" in value:
        import capo_synthetics.types.s3_encryption_config

        out["S3Encryption"] = capo_synthetics.types.s3_encryption_config.serialize_json(
            value["s3_encryption"]
        )
    return out


def deserialize_json(data: dict) -> ArtifactConfigOutput:
    out: ArtifactConfigOutput = {}  # type: ignore[typeddict-item]
    if "S3Encryption" in data:
        import capo_synthetics.types.s3_encryption_config

        out["s3_encryption"] = (
            capo_synthetics.types.s3_encryption_config.deserialize_json(
                data["S3Encryption"]
            )
        )
    return out
