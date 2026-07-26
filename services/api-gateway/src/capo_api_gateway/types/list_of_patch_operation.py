"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfPatchOperation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.patch_operation

ListOfPatchOperation: TypeAlias = list[
    "capo_api_gateway.types.patch_operation.PatchOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfPatchOperation) -> list:
    import capo_api_gateway.types.patch_operation

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.patch_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfPatchOperation:
    import capo_api_gateway.types.patch_operation

    out: ListOfPatchOperation = []
    for item in data:
        out.append(capo_api_gateway.types.patch_operation.deserialize_json(item))
    return out
