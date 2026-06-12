"""Generated from Smithy shape ``com.amazonaws.ssm#PatchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_filter

PatchFilterList: TypeAlias = list["aws_sdk_ssm.types.patch_filter.PatchFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchFilterList) -> list:
    import aws_sdk_ssm.types.patch_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.patch_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchFilterList:
    import aws_sdk_ssm.types.patch_filter

    out: PatchFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.patch_filter.deserialize_aws_json_1_1(item))
    return out
