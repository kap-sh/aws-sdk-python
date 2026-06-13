"""Generated from Smithy shape ``com.amazonaws.devopsagent#CustomHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.custom_header_name
    import aws_sdk_devops_agent.types.custom_header_value

CustomHeaders: TypeAlias = dict[
    "aws_sdk_devops_agent.types.custom_header_name.CustomHeaderName",
    "aws_sdk_devops_agent.types.custom_header_value.CustomHeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomHeaders:
    out: CustomHeaders = {}
    for key, value in data.items():
        out[key] = value
    return out
