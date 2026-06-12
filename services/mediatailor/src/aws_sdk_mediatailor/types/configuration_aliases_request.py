"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigurationAliasesRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string

ConfigurationAliasesRequest: TypeAlias = dict[
    "aws_sdk_mediatailor.types.__string.__string",
    "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConfigurationAliasesRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_mediatailor.types.__map_of__string

        out[key] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ConfigurationAliasesRequest:
    out: ConfigurationAliasesRequest = {}
    for key, value in data.items():
        import aws_sdk_mediatailor.types.__map_of__string

        out[key] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(value)
    return out
