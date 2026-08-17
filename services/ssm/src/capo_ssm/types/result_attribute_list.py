"""Generated from Smithy shape ``com.amazonaws.ssm#ResultAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.result_attribute

ResultAttributeList: TypeAlias = list["capo_ssm.types.result_attribute.ResultAttribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultAttributeList) -> list:
    import capo_ssm.types.result_attribute

    out: list = []
    for item in value:
        out.append(capo_ssm.types.result_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResultAttributeList:
    import capo_ssm.types.result_attribute

    out: ResultAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.result_attribute.deserialize_aws_json_1_1(item))
    return out
