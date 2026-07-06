"""Generated from Smithy shape ``com.amazonaws.signer#HashAlgorithmOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.hash_algorithm
    import aws_sdk_signer.types.hash_algorithms


class HashAlgorithmOptions(TypedDict, closed=True):
    allowed_values: "aws_sdk_signer.types.hash_algorithms.HashAlgorithms"
    """<p>The set of accepted hash algorithms allowed in a code-signing job.</p>"""
    default_value: "aws_sdk_signer.types.hash_algorithm.HashAlgorithm"
    """<p>The default hash algorithm that is used in a code-signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HashAlgorithmOptions) -> dict:
    out: dict = {}
    import aws_sdk_signer.types.hash_algorithms

    out["allowedValues"] = aws_sdk_signer.types.hash_algorithms.serialize_json(
        value["allowed_values"]
    )
    import aws_sdk_signer.types.hash_algorithm

    out["defaultValue"] = aws_sdk_signer.types.hash_algorithm.serialize_json(
        value["default_value"]
    )
    return out


def deserialize_json(data: dict) -> HashAlgorithmOptions:
    out: HashAlgorithmOptions = {}  # type: ignore[typeddict-item]
    if "allowedValues" in data:
        import aws_sdk_signer.types.hash_algorithms

        out["allowed_values"] = aws_sdk_signer.types.hash_algorithms.deserialize_json(
            data["allowedValues"]
        )
    else:
        raise DeserializationError("HashAlgorithmOptions.allowed_values required")
    if "defaultValue" in data:
        import aws_sdk_signer.types.hash_algorithm

        out["default_value"] = aws_sdk_signer.types.hash_algorithm.deserialize_json(
            data["defaultValue"]
        )
    else:
        raise DeserializationError("HashAlgorithmOptions.default_value required")
    return out
