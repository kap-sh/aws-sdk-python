"""Generated from Smithy shape ``com.amazonaws.medialive#SrtCallerDecryptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.algorithm


class SrtCallerDecryptionRequest(TypedDict):
    algorithm: NotRequired["aws_sdk_medialive.types.algorithm.Algorithm"]
    """The algorithm used to encrypt content."""
    passphrase_secret_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN for the secret in Secrets Manager. Someone in your organization must create a secret and provide you with its ARN. This secret holds the passphrase that MediaLive will use to decrypt the source content."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerDecryptionRequest) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import aws_sdk_medialive.types.algorithm

        out["algorithm"] = aws_sdk_medialive.types.algorithm.serialize_json(
            value["algorithm"]
        )
    if "passphrase_secret_arn" in value:
        out["passphraseSecretArn"] = value["passphrase_secret_arn"]
    return out


def deserialize_json(data: dict) -> SrtCallerDecryptionRequest:
    out: SrtCallerDecryptionRequest = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import aws_sdk_medialive.types.algorithm

        out["algorithm"] = aws_sdk_medialive.types.algorithm.deserialize_json(
            data["algorithm"]
        )
    if "passphraseSecretArn" in data:
        out["passphrase_secret_arn"] = data["passphraseSecretArn"]
    return out
