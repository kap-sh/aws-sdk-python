"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.property_key
    import aws_sdk_service_catalog.types.property_value

ProvisionedProductProperties: TypeAlias = dict[
    "aws_sdk_service_catalog.types.property_key.PropertyKey",
    "aws_sdk_service_catalog.types.property_value.PropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProvisionedProductProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_service_catalog.types.property_key

        out[aws_sdk_service_catalog.types.property_key.serialize_aws_json_1_1(key)] = (
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductProperties:
    out: ProvisionedProductProperties = {}
    for key, value in data.items():
        import aws_sdk_service_catalog.types.property_key

        out[
            aws_sdk_service_catalog.types.property_key.deserialize_aws_json_1_1(key)
        ] = value
    return out
