"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemOperationalData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_data_key
    import capo_ssm.types.ops_item_data_value

OpsItemOperationalData: TypeAlias = dict[
    "capo_ssm.types.ops_item_data_key.OpsItemDataKey",
    "capo_ssm.types.ops_item_data_value.OpsItemDataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OpsItemOperationalData) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.ops_item_data_value

        out[key] = capo_ssm.types.ops_item_data_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemOperationalData:
    out: OpsItemOperationalData = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_ssm.types.ops_item_data_value

        out[key] = capo_ssm.types.ops_item_data_value.deserialize_aws_json_1_1(value)
    return out
