"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FunctionsRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.function_request
    import capo_iottwinmaker.types.name

FunctionsRequest: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.function_request.FunctionRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FunctionsRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.function_request

        out[key] = capo_iottwinmaker.types.function_request.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FunctionsRequest:
    out: FunctionsRequest = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.function_request

        out[key] = capo_iottwinmaker.types.function_request.deserialize_json(value)
    return out
