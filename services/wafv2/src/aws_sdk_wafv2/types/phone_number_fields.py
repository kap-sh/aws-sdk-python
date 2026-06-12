"""Generated from Smithy shape ``com.amazonaws.wafv2#PhoneNumberFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.phone_number_field

PhoneNumberFields: TypeAlias = list[
    "aws_sdk_wafv2.types.phone_number_field.PhoneNumberField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhoneNumberFields) -> list:
    import aws_sdk_wafv2.types.phone_number_field

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.phone_number_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PhoneNumberFields:
    import aws_sdk_wafv2.types.phone_number_field

    out: PhoneNumberFields = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.phone_number_field.deserialize_aws_json_1_1(item)
        )
    return out
