"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointCommonAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.http_endpoint_common_attribute

HttpEndpointCommonAttributesList: TypeAlias = list[
    "aws_sdk_firehose.types.http_endpoint_common_attribute.HttpEndpointCommonAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointCommonAttributesList) -> list:
    import aws_sdk_firehose.types.http_endpoint_common_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_firehose.types.http_endpoint_common_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HttpEndpointCommonAttributesList:
    import aws_sdk_firehose.types.http_endpoint_common_attribute

    out: HttpEndpointCommonAttributesList = []
    for item in data:
        out.append(
            aws_sdk_firehose.types.http_endpoint_common_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
