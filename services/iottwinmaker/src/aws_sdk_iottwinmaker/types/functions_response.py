"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FunctionsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.function_response
    import aws_sdk_iottwinmaker.types.name

FunctionsResponse: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.function_response.FunctionResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FunctionsResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.function_response

        out[key] = aws_sdk_iottwinmaker.types.function_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FunctionsResponse:
    out: FunctionsResponse = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.function_response

        out[key] = aws_sdk_iottwinmaker.types.function_response.deserialize_json(value)
    return out
