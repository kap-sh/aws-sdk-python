"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_entity

OpsEntityList: TypeAlias = list["capo_ssm.types.ops_entity.OpsEntity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsEntityList) -> list:
    import capo_ssm.types.ops_entity

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsEntityList:
    import capo_ssm.types.ops_entity

    out: OpsEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_entity.deserialize_aws_json_1_1(item))
    return out
