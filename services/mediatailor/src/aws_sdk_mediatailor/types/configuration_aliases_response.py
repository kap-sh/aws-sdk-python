"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigurationAliasesResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string

ConfigurationAliasesResponse: TypeAlias = dict[
    "aws_sdk_mediatailor.types.__string.__string",
    "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConfigurationAliasesResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_mediatailor.types.__map_of__string

        out[key] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ConfigurationAliasesResponse:
    out: ConfigurationAliasesResponse = {}
    for key, value in data.items():
        import aws_sdk_mediatailor.types.__map_of__string

        out[key] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(value)
    return out
