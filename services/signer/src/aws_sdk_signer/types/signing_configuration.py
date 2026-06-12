"""Generated from Smithy shape ``com.amazonaws.signer#SigningConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.encryption_algorithm_options
    import aws_sdk_signer.types.hash_algorithm_options


class SigningConfiguration(TypedDict):
    encryption_algorithm_options: (
        "aws_sdk_signer.types.encryption_algorithm_options.EncryptionAlgorithmOptions"
    )
    """<p>The encryption algorithm options that are available for a code-signing job.</p>"""
    hash_algorithm_options: (
        "aws_sdk_signer.types.hash_algorithm_options.HashAlgorithmOptions"
    )
    """<p>The hash algorithm options that are available for a code-signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_signer.types.encryption_algorithm_options

    out["encryptionAlgorithmOptions"] = (
        aws_sdk_signer.types.encryption_algorithm_options.serialize_json(
            value["encryption_algorithm_options"]
        )
    )
    import aws_sdk_signer.types.hash_algorithm_options

    out["hashAlgorithmOptions"] = (
        aws_sdk_signer.types.hash_algorithm_options.serialize_json(
            value["hash_algorithm_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> SigningConfiguration:
    out: SigningConfiguration = {}  # type: ignore[typeddict-item]
    if "encryptionAlgorithmOptions" in data:
        import aws_sdk_signer.types.encryption_algorithm_options

        out["encryption_algorithm_options"] = (
            aws_sdk_signer.types.encryption_algorithm_options.deserialize_json(
                data["encryptionAlgorithmOptions"]
            )
        )
    else:
        raise DeserializationError(
            "SigningConfiguration.encryption_algorithm_options required"
        )
    if "hashAlgorithmOptions" in data:
        import aws_sdk_signer.types.hash_algorithm_options

        out["hash_algorithm_options"] = (
            aws_sdk_signer.types.hash_algorithm_options.deserialize_json(
                data["hashAlgorithmOptions"]
            )
        )
    else:
        raise DeserializationError(
            "SigningConfiguration.hash_algorithm_options required"
        )
    return out
