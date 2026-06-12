"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntityItemEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_entity_item_entry

OpsEntityItemEntryList: TypeAlias = list[
    "aws_sdk_ssm.types.ops_entity_item_entry.OpsEntityItemEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsEntityItemEntryList) -> list:
    import aws_sdk_ssm.types.ops_entity_item_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.ops_entity_item_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsEntityItemEntryList:
    import aws_sdk_ssm.types.ops_entity_item_entry

    out: OpsEntityItemEntryList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.ops_entity_item_entry.deserialize_aws_json_1_1(item)
        )
    return out
