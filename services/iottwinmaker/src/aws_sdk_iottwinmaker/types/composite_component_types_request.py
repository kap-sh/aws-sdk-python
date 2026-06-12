"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentTypesRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.composite_component_type_request
    import aws_sdk_iottwinmaker.types.name

CompositeComponentTypesRequest: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.composite_component_type_request.CompositeComponentTypeRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompositeComponentTypesRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.composite_component_type_request

        out[key] = (
            aws_sdk_iottwinmaker.types.composite_component_type_request.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CompositeComponentTypesRequest:
    out: CompositeComponentTypesRequest = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.composite_component_type_request

        out[key] = (
            aws_sdk_iottwinmaker.types.composite_component_type_request.deserialize_json(
                value
            )
        )
    return out
