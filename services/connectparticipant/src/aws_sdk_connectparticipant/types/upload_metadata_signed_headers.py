"""Generated from Smithy shape ``com.amazonaws.connectparticipant#UploadMetadataSignedHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.upload_metadata_signed_headers_key
    import aws_sdk_connectparticipant.types.upload_metadata_signed_headers_value

UploadMetadataSignedHeaders: TypeAlias = dict[
    "aws_sdk_connectparticipant.types.upload_metadata_signed_headers_key.UploadMetadataSignedHeadersKey",
    "aws_sdk_connectparticipant.types.upload_metadata_signed_headers_value.UploadMetadataSignedHeadersValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UploadMetadataSignedHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UploadMetadataSignedHeaders:
    out: UploadMetadataSignedHeaders = {}
    for key, value in data.items():
        out[key] = value
    return out
