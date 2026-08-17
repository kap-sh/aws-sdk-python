"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntityItemMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_entity_item
    import capo_ssm.types.ops_entity_item_key

OpsEntityItemMap: TypeAlias = dict[
    "capo_ssm.types.ops_entity_item_key.OpsEntityItemKey",
    "capo_ssm.types.ops_entity_item.OpsEntityItem",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OpsEntityItemMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.ops_entity_item

        out[key] = capo_ssm.types.ops_entity_item.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsEntityItemMap:
    out: OpsEntityItemMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_ssm.types.ops_entity_item

        out[key] = capo_ssm.types.ops_entity_item.deserialize_aws_json_1_1(value)
    return out
