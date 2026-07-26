"""Generated from Smithy shape ``com.amazonaws.signer#EncryptionAlgorithmOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signer.types.encryption_algorithm
    import capo_signer.types.encryption_algorithms


class EncryptionAlgorithmOptions(TypedDict, closed=True):
    allowed_values: "capo_signer.types.encryption_algorithms.EncryptionAlgorithms"
    """<p>The set of accepted encryption algorithms that are allowed in a code-signing job.</p>"""
    default_value: "capo_signer.types.encryption_algorithm.EncryptionAlgorithm"
    """<p>The default encryption algorithm that is used by a code-signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAlgorithmOptions) -> dict:
    out: dict = {}
    import capo_signer.types.encryption_algorithms

    out["allowedValues"] = capo_signer.types.encryption_algorithms.serialize_json(
        value["allowed_values"]
    )
    import capo_signer.types.encryption_algorithm

    out["defaultValue"] = capo_signer.types.encryption_algorithm.serialize_json(
        value["default_value"]
    )
    return out


def deserialize_json(data: dict) -> EncryptionAlgorithmOptions:
    out: EncryptionAlgorithmOptions = {}  # type: ignore[typeddict-item]
    if "allowedValues" in data:
        import capo_signer.types.encryption_algorithms

        out["allowed_values"] = (
            capo_signer.types.encryption_algorithms.deserialize_json(
                data["allowedValues"]
            )
        )
    else:
        raise DeserializationError("EncryptionAlgorithmOptions.allowed_values required")
    if "defaultValue" in data:
        import capo_signer.types.encryption_algorithm

        out["default_value"] = capo_signer.types.encryption_algorithm.deserialize_json(
            data["defaultValue"]
        )
    else:
        raise DeserializationError("EncryptionAlgorithmOptions.default_value required")
    return out
