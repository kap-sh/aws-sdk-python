"""Generated from Smithy shape ``com.amazonaws.ssm#TargetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.target_map_key
    import aws_sdk_ssm.types.target_map_value_list

TargetMap: TypeAlias = dict[
    "aws_sdk_ssm.types.target_map_key.TargetMapKey",
    "aws_sdk_ssm.types.target_map_value_list.TargetMapValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TargetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.target_map_value_list

        out[key] = aws_sdk_ssm.types.target_map_value_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetMap:
    out: TargetMap = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.target_map_value_list

        out[key] = aws_sdk_ssm.types.target_map_value_list.deserialize_aws_json_1_1(
            value
        )
    return out
