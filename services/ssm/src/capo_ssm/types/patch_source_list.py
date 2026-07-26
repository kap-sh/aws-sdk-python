"""Generated from Smithy shape ``com.amazonaws.ssm#PatchSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_source

PatchSourceList: TypeAlias = list["capo_ssm.types.patch_source.PatchSource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchSourceList) -> list:
    import capo_ssm.types.patch_source

    out: list = []
    for item in value:
        out.append(capo_ssm.types.patch_source.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchSourceList:
    import capo_ssm.types.patch_source

    out: PatchSourceList = []
    for item in data:
        out.append(capo_ssm.types.patch_source.deserialize_aws_json_1_1(item))
    return out
