"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#Definitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.definition

Definitions: TypeAlias = list["aws_sdk_sagemaker_edge.types.definition.Definition"]


# --- restJson1 ser/de ---
def serialize_json(value: Definitions) -> list:
    import aws_sdk_sagemaker_edge.types.definition

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_edge.types.definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> Definitions:
    import aws_sdk_sagemaker_edge.types.definition

    out: Definitions = []
    for item in data:
        out.append(aws_sdk_sagemaker_edge.types.definition.deserialize_json(item))
    return out
