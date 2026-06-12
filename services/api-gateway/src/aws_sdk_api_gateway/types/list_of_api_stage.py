"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfApiStage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.api_stage

ListOfApiStage: TypeAlias = list["aws_sdk_api_gateway.types.api_stage.ApiStage"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfApiStage) -> list:
    import aws_sdk_api_gateway.types.api_stage

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.api_stage.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfApiStage:
    import aws_sdk_api_gateway.types.api_stage

    out: ListOfApiStage = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.api_stage.deserialize_json(item))
    return out
