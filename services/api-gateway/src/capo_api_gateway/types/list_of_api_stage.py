"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfApiStage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.api_stage

ListOfApiStage: TypeAlias = list["capo_api_gateway.types.api_stage.ApiStage"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfApiStage) -> list:
    import capo_api_gateway.types.api_stage

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.api_stage.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfApiStage:
    import capo_api_gateway.types.api_stage

    out: ListOfApiStage = []
    for item in data:
        out.append(capo_api_gateway.types.api_stage.deserialize_json(item))
    return out
