"""Generated from Smithy shape ``com.amazonaws.mediapackage#CmafEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.cmaf_encryption_method
    import aws_sdk_mediapackage.types.speke_key_provider


class CmafEncryption(TypedDict, closed=True):
    constant_initialization_vector: NotRequired[
        "aws_sdk_mediapackage.types.__string.__string"
    ]
    """An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV)."""
    encryption_method: NotRequired[
        "aws_sdk_mediapackage.types.cmaf_encryption_method.CmafEncryptionMethod"
    ]
    key_rotation_interval_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Time (in seconds) between each encryption key rotation."""
    speke_key_provider: NotRequired[
        "aws_sdk_mediapackage.types.speke_key_provider.SpekeKeyProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CmafEncryption) -> dict:
    out: dict = {}
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "encryption_method" in value:
        import aws_sdk_mediapackage.types.cmaf_encryption_method

        out["encryptionMethod"] = (
            aws_sdk_mediapackage.types.cmaf_encryption_method.serialize_json(
                value["encryption_method"]
            )
        )
    if "key_rotation_interval_seconds" in value:
        out["keyRotationIntervalSeconds"] = value["key_rotation_interval_seconds"]
    if "speke_key_provider" in value:
        import aws_sdk_mediapackage.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediapackage.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafEncryption:
    out: CmafEncryption = {}  # type: ignore[typeddict-item]
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "encryptionMethod" in data:
        import aws_sdk_mediapackage.types.cmaf_encryption_method

        out["encryption_method"] = (
            aws_sdk_mediapackage.types.cmaf_encryption_method.deserialize_json(
                data["encryptionMethod"]
            )
        )
    if "keyRotationIntervalSeconds" in data:
        out["key_rotation_interval_seconds"] = data["keyRotationIntervalSeconds"]
    if "spekeKeyProvider" in data:
        import aws_sdk_mediapackage.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediapackage.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
