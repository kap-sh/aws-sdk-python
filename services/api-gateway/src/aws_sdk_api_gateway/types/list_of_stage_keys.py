"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfStageKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.stage_key

ListOfStageKeys: TypeAlias = list["aws_sdk_api_gateway.types.stage_key.StageKey"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfStageKeys) -> list:
    import aws_sdk_api_gateway.types.stage_key

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.stage_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfStageKeys:
    import aws_sdk_api_gateway.types.stage_key

    out: ListOfStageKeys = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.stage_key.deserialize_json(item))
    return out
