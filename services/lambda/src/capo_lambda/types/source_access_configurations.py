"""Generated from Smithy shape ``com.amazonaws.lambda#SourceAccessConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.source_access_configuration

SourceAccessConfigurations: TypeAlias = list[
    "capo_lambda.types.source_access_configuration.SourceAccessConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceAccessConfigurations) -> list:
    import capo_lambda.types.source_access_configuration

    out: list = []
    for item in value:
        out.append(capo_lambda.types.source_access_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceAccessConfigurations:
    import capo_lambda.types.source_access_configuration

    out: SourceAccessConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.source_access_configuration.deserialize_json(item))
    return out
