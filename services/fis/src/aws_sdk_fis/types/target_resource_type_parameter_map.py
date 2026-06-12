"""Generated from Smithy shape ``com.amazonaws.fis#TargetResourceTypeParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_resource_type_parameter
    import aws_sdk_fis.types.target_resource_type_parameter_name

TargetResourceTypeParameterMap: TypeAlias = dict[
    "aws_sdk_fis.types.target_resource_type_parameter_name.TargetResourceTypeParameterName",
    "aws_sdk_fis.types.target_resource_type_parameter.TargetResourceTypeParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TargetResourceTypeParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fis.types.target_resource_type_parameter

        out[key] = aws_sdk_fis.types.target_resource_type_parameter.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> TargetResourceTypeParameterMap:
    out: TargetResourceTypeParameterMap = {}
    for key, value in data.items():
        import aws_sdk_fis.types.target_resource_type_parameter

        out[key] = aws_sdk_fis.types.target_resource_type_parameter.deserialize_json(
            value
        )
    return out
