"""Generated from Smithy shape ``com.amazonaws.lambda#SourceAccessConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.source_access_configuration

SourceAccessConfigurations: TypeAlias = list[
    "aws_sdk_lambda.types.source_access_configuration.SourceAccessConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceAccessConfigurations) -> list:
    import aws_sdk_lambda.types.source_access_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lambda.types.source_access_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SourceAccessConfigurations:
    import aws_sdk_lambda.types.source_access_configuration

    out: SourceAccessConfigurations = []
    for item in data:
        out.append(
            aws_sdk_lambda.types.source_access_configuration.deserialize_json(item)
        )
    return out
