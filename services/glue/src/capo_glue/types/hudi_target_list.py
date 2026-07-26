"""Generated from Smithy shape ``com.amazonaws.glue#HudiTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.hudi_target

HudiTargetList: TypeAlias = list["capo_glue.types.hudi_target.HudiTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HudiTargetList) -> list:
    import capo_glue.types.hudi_target

    out: list = []
    for item in value:
        out.append(capo_glue.types.hudi_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HudiTargetList:
    import capo_glue.types.hudi_target

    out: HudiTargetList = []
    for item in data:
        out.append(capo_glue.types.hudi_target.deserialize_aws_json_1_1(item))
    return out
