"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#SetAttribute``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.attribute_value

SetAttribute: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.attribute_value.AttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetAttribute) -> list:
    import aws_sdk_verifiedpermissions.types.attribute_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.attribute_value.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SetAttribute:
    import aws_sdk_verifiedpermissions.types.attribute_value

    out: SetAttribute = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.attribute_value.deserialize_aws_json_1_0(
                item
            )
        )
    return out
