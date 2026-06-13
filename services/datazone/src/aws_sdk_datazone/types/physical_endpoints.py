"""Generated from Smithy shape ``com.amazonaws.datazone#PhysicalEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.physical_endpoint

PhysicalEndpoints: TypeAlias = list[
    "aws_sdk_datazone.types.physical_endpoint.PhysicalEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalEndpoints) -> list:
    import aws_sdk_datazone.types.physical_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.physical_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhysicalEndpoints:
    import aws_sdk_datazone.types.physical_endpoint

    out: PhysicalEndpoints = []
    for item in data:
        out.append(aws_sdk_datazone.types.physical_endpoint.deserialize_json(item))
    return out
