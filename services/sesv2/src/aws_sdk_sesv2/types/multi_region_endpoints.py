"""Generated from Smithy shape ``com.amazonaws.sesv2#MultiRegionEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.multi_region_endpoint

MultiRegionEndpoints: TypeAlias = list[
    "aws_sdk_sesv2.types.multi_region_endpoint.MultiRegionEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiRegionEndpoints) -> list:
    import aws_sdk_sesv2.types.multi_region_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.multi_region_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiRegionEndpoints:
    import aws_sdk_sesv2.types.multi_region_endpoint

    out: MultiRegionEndpoints = []
    for item in data:
        out.append(aws_sdk_sesv2.types.multi_region_endpoint.deserialize_json(item))
    return out
