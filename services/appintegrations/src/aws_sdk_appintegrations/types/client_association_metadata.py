"""Generated from Smithy shape ``com.amazonaws.appintegrations#ClientAssociationMetadata``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.non_blank_string

ClientAssociationMetadata: TypeAlias = dict["aws_sdk_appintegrations.types.non_blank_string.NonBlankString", "aws_sdk_appintegrations.types.non_blank_string.NonBlankString"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ClientAssociationMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ClientAssociationMetadata:
    out: ClientAssociationMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out