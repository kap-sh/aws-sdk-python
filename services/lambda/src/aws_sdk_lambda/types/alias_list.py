"""Generated from Smithy shape ``com.amazonaws.lambda#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.alias_configuration

AliasList: TypeAlias = list[
    "aws_sdk_lambda.types.alias_configuration.AliasConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AliasList) -> list:
    import aws_sdk_lambda.types.alias_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.alias_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AliasList:
    import aws_sdk_lambda.types.alias_configuration

    out: AliasList = []
    for item in data:
        out.append(aws_sdk_lambda.types.alias_configuration.deserialize_json(item))
    return out
