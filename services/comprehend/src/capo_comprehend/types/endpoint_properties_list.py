"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.endpoint_properties

EndpointPropertiesList: TypeAlias = list[
    "capo_comprehend.types.endpoint_properties.EndpointProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointPropertiesList) -> list:
    import capo_comprehend.types.endpoint_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.endpoint_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointPropertiesList:
    import capo_comprehend.types.endpoint_properties

    out: EndpointPropertiesList = []
    for item in data:
        out.append(
            capo_comprehend.types.endpoint_properties.deserialize_aws_json_1_1(item)
        )
    return out
