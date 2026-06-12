"""Generated from Smithy shape ``com.amazonaws.connect#UrlMetadataSignedHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.url_metadata_signed_headers_key
    import aws_sdk_connect.types.url_metadata_signed_headers_value

UrlMetadataSignedHeaders: TypeAlias = dict[
    "aws_sdk_connect.types.url_metadata_signed_headers_key.UrlMetadataSignedHeadersKey",
    "aws_sdk_connect.types.url_metadata_signed_headers_value.UrlMetadataSignedHeadersValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UrlMetadataSignedHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UrlMetadataSignedHeaders:
    out: UrlMetadataSignedHeaders = {}
    for key, value in data.items():
        out[key] = value
    return out
