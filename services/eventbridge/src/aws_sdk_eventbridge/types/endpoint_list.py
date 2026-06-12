"""Generated from Smithy shape ``com.amazonaws.eventbridge#EndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.endpoint

EndpointList: TypeAlias = list["aws_sdk_eventbridge.types.endpoint.Endpoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointList) -> list:
    import aws_sdk_eventbridge.types.endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_eventbridge.types.endpoint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointList:
    import aws_sdk_eventbridge.types.endpoint

    out: EndpointList = []
    for item in data:
        out.append(aws_sdk_eventbridge.types.endpoint.deserialize_aws_json_1_1(item))
    return out
