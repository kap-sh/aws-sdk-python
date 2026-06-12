"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemOperationalData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_data_key
    import aws_sdk_ssm.types.ops_item_data_value

OpsItemOperationalData: TypeAlias = dict[
    "aws_sdk_ssm.types.ops_item_data_key.OpsItemDataKey",
    "aws_sdk_ssm.types.ops_item_data_value.OpsItemDataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OpsItemOperationalData) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.ops_item_data_value

        out[key] = aws_sdk_ssm.types.ops_item_data_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemOperationalData:
    out: OpsItemOperationalData = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.ops_item_data_value

        out[key] = aws_sdk_ssm.types.ops_item_data_value.deserialize_aws_json_1_1(value)
    return out
