"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfSdkConfigurationProperty``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.sdk_configuration_property

ListOfSdkConfigurationProperty: TypeAlias = list[
    "aws_sdk_api_gateway.types.sdk_configuration_property.SdkConfigurationProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSdkConfigurationProperty) -> list:
    import aws_sdk_api_gateway.types.sdk_configuration_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_api_gateway.types.sdk_configuration_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfSdkConfigurationProperty:
    import aws_sdk_api_gateway.types.sdk_configuration_property

    out: ListOfSdkConfigurationProperty = []
    for item in data:
        out.append(
            aws_sdk_api_gateway.types.sdk_configuration_property.deserialize_json(item)
        )
    return out
