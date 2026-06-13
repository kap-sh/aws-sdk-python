"""Generated from Smithy shape ``com.amazonaws.groundstation#EndpointDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.endpoint_details

EndpointDetailsList: TypeAlias = list[
    "aws_sdk_groundstation.types.endpoint_details.EndpointDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDetailsList) -> list:
    import aws_sdk_groundstation.types.endpoint_details

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.endpoint_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> EndpointDetailsList:
    import aws_sdk_groundstation.types.endpoint_details

    out: EndpointDetailsList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.endpoint_details.deserialize_json(item))
    return out
