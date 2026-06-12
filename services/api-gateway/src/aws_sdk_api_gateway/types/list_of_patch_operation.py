"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfPatchOperation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.patch_operation

ListOfPatchOperation: TypeAlias = list[
    "aws_sdk_api_gateway.types.patch_operation.PatchOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfPatchOperation) -> list:
    import aws_sdk_api_gateway.types.patch_operation

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.patch_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfPatchOperation:
    import aws_sdk_api_gateway.types.patch_operation

    out: ListOfPatchOperation = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.patch_operation.deserialize_json(item))
    return out
