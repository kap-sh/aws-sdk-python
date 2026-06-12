"""Generated from Smithy shape ``com.amazonaws.glue#HudiTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.hudi_target

HudiTargetList: TypeAlias = list["aws_sdk_glue.types.hudi_target.HudiTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HudiTargetList) -> list:
    import aws_sdk_glue.types.hudi_target

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.hudi_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HudiTargetList:
    import aws_sdk_glue.types.hudi_target

    out: HudiTargetList = []
    for item in data:
        out.append(aws_sdk_glue.types.hudi_target.deserialize_aws_json_1_1(item))
    return out
