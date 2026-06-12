"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssetHashes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.hash_algorithm
    import aws_sdk_codeartifact.types.hash_value

AssetHashes: TypeAlias = dict[
    "aws_sdk_codeartifact.types.hash_algorithm.HashAlgorithm",
    "aws_sdk_codeartifact.types.hash_value.HashValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AssetHashes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_codeartifact.types.hash_algorithm

        out[aws_sdk_codeartifact.types.hash_algorithm.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> AssetHashes:
    out: AssetHashes = {}
    for key, value in data.items():
        import aws_sdk_codeartifact.types.hash_algorithm

        out[aws_sdk_codeartifact.types.hash_algorithm.deserialize_json(key)] = value
    return out
