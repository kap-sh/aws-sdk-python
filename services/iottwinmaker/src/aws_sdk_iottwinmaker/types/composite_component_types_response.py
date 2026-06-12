"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentTypesResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.composite_component_type_response
    import aws_sdk_iottwinmaker.types.name

CompositeComponentTypesResponse: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.composite_component_type_response.CompositeComponentTypeResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompositeComponentTypesResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.composite_component_type_response

        out[key] = (
            aws_sdk_iottwinmaker.types.composite_component_type_response.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CompositeComponentTypesResponse:
    out: CompositeComponentTypesResponse = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.composite_component_type_response

        out[key] = (
            aws_sdk_iottwinmaker.types.composite_component_type_response.deserialize_json(
                value
            )
        )
    return out
