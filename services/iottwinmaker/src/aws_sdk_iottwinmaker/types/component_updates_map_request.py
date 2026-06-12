"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentUpdatesMapRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_update_request
    import aws_sdk_iottwinmaker.types.name

ComponentUpdatesMapRequest: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.component_update_request.ComponentUpdateRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentUpdatesMapRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.component_update_request

        out[key] = aws_sdk_iottwinmaker.types.component_update_request.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ComponentUpdatesMapRequest:
    out: ComponentUpdatesMapRequest = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.component_update_request

        out[key] = aws_sdk_iottwinmaker.types.component_update_request.deserialize_json(
            value
        )
    return out
