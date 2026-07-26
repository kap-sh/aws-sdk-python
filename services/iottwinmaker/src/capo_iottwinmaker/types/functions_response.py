"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FunctionsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.function_response
    import capo_iottwinmaker.types.name

FunctionsResponse: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.function_response.FunctionResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FunctionsResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.function_response

        out[key] = capo_iottwinmaker.types.function_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FunctionsResponse:
    out: FunctionsResponse = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.function_response

        out[key] = capo_iottwinmaker.types.function_response.deserialize_json(value)
    return out
