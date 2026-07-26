"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfBasePathMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.base_path_mapping

ListOfBasePathMapping: TypeAlias = list[
    "capo_api_gateway.types.base_path_mapping.BasePathMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfBasePathMapping) -> list:
    import capo_api_gateway.types.base_path_mapping

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.base_path_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfBasePathMapping:
    import capo_api_gateway.types.base_path_mapping

    out: ListOfBasePathMapping = []
    for item in data:
        out.append(capo_api_gateway.types.base_path_mapping.deserialize_json(item))
    return out
