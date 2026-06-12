"""Generated from Smithy shape ``com.amazonaws.connect#S3Config``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.bucket_name
    import aws_sdk_connect.types.encryption_config
    import aws_sdk_connect.types.prefix


class S3Config(TypedDict):
    bucket_name: "aws_sdk_connect.types.bucket_name.BucketName"
    """<p>The S3 bucket name.</p>"""
    bucket_prefix: "aws_sdk_connect.types.prefix.Prefix"
    """<p>The S3 bucket prefix.</p>"""
    encryption_config: NotRequired[
        "aws_sdk_connect.types.encryption_config.EncryptionConfig"
    ]
    """<p>The Amazon S3 encryption configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Config) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["BucketPrefix"] = value["bucket_prefix"]
    if "encryption_config" in value:
        import aws_sdk_connect.types.encryption_config

        out["EncryptionConfig"] = (
            aws_sdk_connect.types.encryption_config.serialize_json(
                value["encryption_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Config.bucket_name required")
    if "BucketPrefix" in data:
        out["bucket_prefix"] = data["BucketPrefix"]
    else:
        raise DeserializationError("S3Config.bucket_prefix required")
    if "EncryptionConfig" in data:
        import aws_sdk_connect.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_connect.types.encryption_config.deserialize_json(
                data["EncryptionConfig"]
            )
        )
    return out
