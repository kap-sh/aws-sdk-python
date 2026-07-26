"""Generated from Smithy shape ``com.amazonaws.signer#SigningConfigurationOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.encryption_algorithm
    import capo_signer.types.hash_algorithm


class SigningConfigurationOverrides(TypedDict, closed=True):
    encryption_algorithm: NotRequired[
        "capo_signer.types.encryption_algorithm.EncryptionAlgorithm"
    ]
    """<p>A specified override of the default encryption algorithm that is used in a code-signing job.</p>"""
    hash_algorithm: NotRequired["capo_signer.types.hash_algorithm.HashAlgorithm"]
    """<p>A specified override of the default hash algorithm that is used in a code-signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningConfigurationOverrides) -> dict:
    out: dict = {}
    if "encryption_algorithm" in value:
        import capo_signer.types.encryption_algorithm

        out["encryptionAlgorithm"] = (
            capo_signer.types.encryption_algorithm.serialize_json(
                value["encryption_algorithm"]
            )
        )
    if "hash_algorithm" in value:
        import capo_signer.types.hash_algorithm

        out["hashAlgorithm"] = capo_signer.types.hash_algorithm.serialize_json(
            value["hash_algorithm"]
        )
    return out


def deserialize_json(data: dict) -> SigningConfigurationOverrides:
    out: SigningConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if "encryptionAlgorithm" in data:
        import capo_signer.types.encryption_algorithm

        out["encryption_algorithm"] = (
            capo_signer.types.encryption_algorithm.deserialize_json(
                data["encryptionAlgorithm"]
            )
        )
    if "hashAlgorithm" in data:
        import capo_signer.types.hash_algorithm

        out["hash_algorithm"] = capo_signer.types.hash_algorithm.deserialize_json(
            data["hashAlgorithm"]
        )
    return out
