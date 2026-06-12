"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VpcEndpointErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_error

VpcEndpointErrorList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.vpc_endpoint_error.VpcEndpointError"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointErrorList) -> list:
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.vpc_endpoint_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VpcEndpointErrorList:
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_error

    out: VpcEndpointErrorList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.vpc_endpoint_error.deserialize_json(
                item
            )
        )
    return out
