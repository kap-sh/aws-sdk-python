"""Generated from Smithy shape ``com.amazonaws.ssm#OpsResultAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_result_attribute

OpsResultAttributeList: TypeAlias = list[
    "capo_ssm.types.ops_result_attribute.OpsResultAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsResultAttributeList) -> list:
    import capo_ssm.types.ops_result_attribute

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_result_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsResultAttributeList:
    import capo_ssm.types.ops_result_attribute

    out: OpsResultAttributeList = []
    for item in data:
        out.append(capo_ssm.types.ops_result_attribute.deserialize_aws_json_1_1(item))
    return out
