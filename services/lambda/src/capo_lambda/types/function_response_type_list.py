"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionResponseTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.function_response_type

FunctionResponseTypeList: TypeAlias = list[
    "capo_lambda.types.function_response_type.FunctionResponseType"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionResponseTypeList) -> list:
    import capo_lambda.types.function_response_type

    out: list = []
    for item in value:
        out.append(capo_lambda.types.function_response_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionResponseTypeList:
    import capo_lambda.types.function_response_type

    out: FunctionResponseTypeList = []
    for item in data:
        out.append(capo_lambda.types.function_response_type.deserialize_json(item))
    return out
