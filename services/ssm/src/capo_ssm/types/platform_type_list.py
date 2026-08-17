"""Generated from Smithy shape ``com.amazonaws.ssm#PlatformTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.platform_type

PlatformTypeList: TypeAlias = list["capo_ssm.types.platform_type.PlatformType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformTypeList) -> list:
    import capo_ssm.types.platform_type

    out: list = []
    for item in value:
        out.append(capo_ssm.types.platform_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlatformTypeList:
    import capo_ssm.types.platform_type

    out: PlatformTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.platform_type.deserialize_aws_json_1_1(item))
    return out
