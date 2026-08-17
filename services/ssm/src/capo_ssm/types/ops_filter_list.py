"""Generated from Smithy shape ``com.amazonaws.ssm#OpsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_filter

OpsFilterList: TypeAlias = list["capo_ssm.types.ops_filter.OpsFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsFilterList) -> list:
    import capo_ssm.types.ops_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsFilterList:
    import capo_ssm.types.ops_filter

    out: OpsFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_filter.deserialize_aws_json_1_1(item))
    return out
