"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfStage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.stage

ListOfStage: TypeAlias = list["aws_sdk_api_gateway.types.stage.Stage"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfStage) -> list:
    import aws_sdk_api_gateway.types.stage

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.stage.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfStage:
    import aws_sdk_api_gateway.types.stage

    out: ListOfStage = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.stage.deserialize_json(item))
    return out
