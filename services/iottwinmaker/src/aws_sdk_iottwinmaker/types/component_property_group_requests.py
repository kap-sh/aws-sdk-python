"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentPropertyGroupRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_property_group_request
    import aws_sdk_iottwinmaker.types.name

ComponentPropertyGroupRequests: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.component_property_group_request.ComponentPropertyGroupRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentPropertyGroupRequests) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.component_property_group_request

        out[key] = (
            aws_sdk_iottwinmaker.types.component_property_group_request.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentPropertyGroupRequests:
    out: ComponentPropertyGroupRequests = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.component_property_group_request

        out[key] = (
            aws_sdk_iottwinmaker.types.component_property_group_request.deserialize_json(
                value
            )
        )
    return out
