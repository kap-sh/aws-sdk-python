"""Generated from Smithy shape ``com.amazonaws.connect#EmailHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_header_type
    import aws_sdk_connect.types.email_header_value

EmailHeaders: TypeAlias = dict[
    "aws_sdk_connect.types.email_header_type.EmailHeaderType",
    "aws_sdk_connect.types.email_header_value.EmailHeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EmailHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.email_header_type

        out[aws_sdk_connect.types.email_header_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> EmailHeaders:
    out: EmailHeaders = {}
    for key, value in data.items():
        import aws_sdk_connect.types.email_header_type

        out[aws_sdk_connect.types.email_header_type.deserialize_json(key)] = value
    return out
