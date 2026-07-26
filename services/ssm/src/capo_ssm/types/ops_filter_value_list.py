"""Generated from Smithy shape ``com.amazonaws.ssm#OpsFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_filter_value

OpsFilterValueList: TypeAlias = list["capo_ssm.types.ops_filter_value.OpsFilterValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsFilterValueList:
    return list(data)
