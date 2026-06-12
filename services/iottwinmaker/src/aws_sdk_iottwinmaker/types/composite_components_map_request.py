"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentsMapRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.composite_component_request

CompositeComponentsMapRequest: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.component_path.ComponentPath",
    "aws_sdk_iottwinmaker.types.composite_component_request.CompositeComponentRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompositeComponentsMapRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.composite_component_request

        out[key] = (
            aws_sdk_iottwinmaker.types.composite_component_request.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> CompositeComponentsMapRequest:
    out: CompositeComponentsMapRequest = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.composite_component_request

        out[key] = (
            aws_sdk_iottwinmaker.types.composite_component_request.deserialize_json(
                value
            )
        )
    return out
