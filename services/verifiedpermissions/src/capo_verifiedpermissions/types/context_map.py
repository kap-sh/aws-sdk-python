"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.attribute_value

ContextMap: TypeAlias = dict[
    "str", "capo_verifiedpermissions.types.attribute_value.AttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_verifiedpermissions.types.attribute_value

        out[key] = (
            capo_verifiedpermissions.types.attribute_value.serialize_aws_json_1_0(value)
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextMap:
    out: ContextMap = {}
    for key, value in data.items():
        import capo_verifiedpermissions.types.attribute_value

        out[key] = (
            capo_verifiedpermissions.types.attribute_value.deserialize_aws_json_1_0(
                value
            )
        )
    return out
