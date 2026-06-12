"""Generated from Smithy shape ``com.amazonaws.wafv2#AddressFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.address_field

AddressFields: TypeAlias = list["aws_sdk_wafv2.types.address_field.AddressField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddressFields) -> list:
    import aws_sdk_wafv2.types.address_field

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.address_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AddressFields:
    import aws_sdk_wafv2.types.address_field

    out: AddressFields = []
    for item in data:
        out.append(aws_sdk_wafv2.types.address_field.deserialize_aws_json_1_1(item))
    return out
