"""Generated from Smithy shape ``com.amazonaws.amplify#FileMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.file_name
    import aws_sdk_amplify.types.md5_hash

FileMap: TypeAlias = dict[
    "aws_sdk_amplify.types.file_name.FileName", "aws_sdk_amplify.types.md5_hash.MD5Hash"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FileMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FileMap:
    out: FileMap = {}
    for key, value in data.items():
        out[key] = value
    return out
