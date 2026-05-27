"""Generated from Smithy shape ``com.amazonaws.lambda#ArchitecturesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.architecture

ArchitecturesList: TypeAlias = list["aws_sdk_lambda.types.architecture.Architecture"]


# --- restJson1 ser/de ---
def serialize_json(value: ArchitecturesList) -> list:
    import aws_sdk_lambda.types.architecture

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.architecture.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArchitecturesList:
    import aws_sdk_lambda.types.architecture

    out: ArchitecturesList = []
    for item in data:
        out.append(aws_sdk_lambda.types.architecture.deserialize_json(item))
    return out
