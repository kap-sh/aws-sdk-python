"""Generated from Smithy shape ``com.amazonaws.ssm#OpsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_filter

OpsFilterList: TypeAlias = list["aws_sdk_ssm.types.ops_filter.OpsFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsFilterList) -> list:
    import aws_sdk_ssm.types.ops_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.ops_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsFilterList:
    import aws_sdk_ssm.types.ops_filter

    out: OpsFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.ops_filter.deserialize_aws_json_1_1(item))
    return out
