"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MetaData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.attribute_name
    import aws_sdk_iot_managed_integrations.types.attribute_value

MetaData: TypeAlias = dict[
    "aws_sdk_iot_managed_integrations.types.attribute_name.AttributeName",
    "aws_sdk_iot_managed_integrations.types.attribute_value.AttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetaData) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MetaData:
    out: MetaData = {}
    for key, value in data.items():
        out[key] = value
    return out
