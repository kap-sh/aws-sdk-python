"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.endpoint_properties

EndpointPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.endpoint_properties.EndpointProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointPropertiesList) -> list:
    import aws_sdk_comprehend.types.endpoint_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.endpoint_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointPropertiesList:
    import aws_sdk_comprehend.types.endpoint_properties

    out: EndpointPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.endpoint_properties.deserialize_aws_json_1_1(item)
        )
    return out
