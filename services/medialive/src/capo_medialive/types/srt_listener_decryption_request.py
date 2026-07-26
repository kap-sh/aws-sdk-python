"""Generated from Smithy shape ``com.amazonaws.medialive#SrtListenerDecryptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.algorithm


class SrtListenerDecryptionRequest(TypedDict, closed=True):
    algorithm: NotRequired["capo_medialive.types.algorithm.Algorithm"]
    """Required. The decryption algorithm."""
    passphrase_secret_arn: NotRequired["capo_medialive.types.__string.__string"]
    """Required. The ARN for the secret in Secrets Manager that holds the passphrase."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerDecryptionRequest) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import capo_medialive.types.algorithm

        out["algorithm"] = capo_medialive.types.algorithm.serialize_json(
            value["algorithm"]
        )
    if "passphrase_secret_arn" in value:
        out["passphraseSecretArn"] = value["passphrase_secret_arn"]
    return out


def deserialize_json(data: dict) -> SrtListenerDecryptionRequest:
    out: SrtListenerDecryptionRequest = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import capo_medialive.types.algorithm

        out["algorithm"] = capo_medialive.types.algorithm.deserialize_json(
            data["algorithm"]
        )
    if "passphraseSecretArn" in data:
        out["passphrase_secret_arn"] = data["passphraseSecretArn"]
    return out
