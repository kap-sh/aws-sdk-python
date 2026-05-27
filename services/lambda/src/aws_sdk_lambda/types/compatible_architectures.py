"""Generated from Smithy shape ``com.amazonaws.lambda#CompatibleArchitectures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.architecture

CompatibleArchitectures: TypeAlias = list[
    "aws_sdk_lambda.types.architecture.Architecture"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleArchitectures) -> list:
    import aws_sdk_lambda.types.architecture

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.architecture.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompatibleArchitectures:
    import aws_sdk_lambda.types.architecture

    out: CompatibleArchitectures = []
    for item in data:
        out.append(aws_sdk_lambda.types.architecture.deserialize_json(item))
    return out
