"""Generated from Smithy shape ``com.amazonaws.glue#DevEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.dev_endpoint

DevEndpointList: TypeAlias = list["aws_sdk_glue.types.dev_endpoint.DevEndpoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevEndpointList) -> list:
    import aws_sdk_glue.types.dev_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.dev_endpoint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DevEndpointList:
    import aws_sdk_glue.types.dev_endpoint

    out: DevEndpointList = []
    for item in data:
        out.append(aws_sdk_glue.types.dev_endpoint.deserialize_aws_json_1_1(item))
    return out
