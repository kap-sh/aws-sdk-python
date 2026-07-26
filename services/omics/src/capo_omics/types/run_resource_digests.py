"""Generated from Smithy shape ``com.amazonaws.omics#RunResourceDigests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.run_resource_digest
    import capo_omics.types.run_resource_digest_key

RunResourceDigests: TypeAlias = dict[
    "capo_omics.types.run_resource_digest_key.RunResourceDigestKey",
    "capo_omics.types.run_resource_digest.RunResourceDigest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RunResourceDigests) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RunResourceDigests:
    out: RunResourceDigests = {}
    for key, value in data.items():
        out[key] = value
    return out
