"""Generated from Smithy shape ``com.amazonaws.iot#DocumentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.document_parameter

DocumentParameters: TypeAlias = list[
    "aws_sdk_iot.types.document_parameter.DocumentParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentParameters) -> list:
    import aws_sdk_iot.types.document_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.document_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentParameters:
    import aws_sdk_iot.types.document_parameter

    out: DocumentParameters = []
    for item in data:
        out.append(aws_sdk_iot.types.document_parameter.deserialize_json(item))
    return out
