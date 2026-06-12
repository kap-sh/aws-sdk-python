"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#EndpointsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.service_url
    import aws_sdk_elasticsearch_service.types.string

EndpointsMap: TypeAlias = dict[
    "aws_sdk_elasticsearch_service.types.string.String",
    "aws_sdk_elasticsearch_service.types.service_url.ServiceUrl",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EndpointsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EndpointsMap:
    out: EndpointsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
