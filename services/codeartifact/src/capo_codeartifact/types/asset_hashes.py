"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssetHashes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.hash_algorithm
    import capo_codeartifact.types.hash_value

AssetHashes: TypeAlias = dict[
    "capo_codeartifact.types.hash_algorithm.HashAlgorithm",
    "capo_codeartifact.types.hash_value.HashValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AssetHashes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeartifact.types.hash_algorithm

        out[capo_codeartifact.types.hash_algorithm.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> AssetHashes:
    out: AssetHashes = {}
    for key, value in data.items():
        import capo_codeartifact.types.hash_algorithm

        out[capo_codeartifact.types.hash_algorithm.deserialize_json(key)] = value
    return out
