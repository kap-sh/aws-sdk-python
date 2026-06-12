"""Generated from Smithy shape ``com.amazonaws.signer#HashAlgorithms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.hash_algorithm

HashAlgorithms: TypeAlias = list["aws_sdk_signer.types.hash_algorithm.HashAlgorithm"]


# --- restJson1 ser/de ---
def serialize_json(value: HashAlgorithms) -> list:
    import aws_sdk_signer.types.hash_algorithm

    out: list = []
    for item in value:
        out.append(aws_sdk_signer.types.hash_algorithm.serialize_json(item))
    return out


def deserialize_json(data: list) -> HashAlgorithms:
    import aws_sdk_signer.types.hash_algorithm

    out: HashAlgorithms = []
    for item in data:
        out.append(aws_sdk_signer.types.hash_algorithm.deserialize_json(item))
    return out
