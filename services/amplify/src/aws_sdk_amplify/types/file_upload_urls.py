"""Generated from Smithy shape ``com.amazonaws.amplify#FileUploadUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.file_name
    import aws_sdk_amplify.types.upload_url

FileUploadUrls: TypeAlias = dict[
    "aws_sdk_amplify.types.file_name.FileName",
    "aws_sdk_amplify.types.upload_url.UploadUrl",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FileUploadUrls) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FileUploadUrls:
    out: FileUploadUrls = {}
    for key, value in data.items():
        out[key] = value
    return out
