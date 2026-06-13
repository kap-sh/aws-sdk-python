"""Generated from Smithy shape ``com.amazonaws.omics#FormatToHeader``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.format_to_header_key

FormatToHeader: TypeAlias = dict[
    "aws_sdk_omics.types.format_to_header_key.FormatToHeaderKey", "str"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormatToHeader) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FormatToHeader:
    out: FormatToHeader = {}
    for key, value in data.items():
        out[key] = value
    return out
