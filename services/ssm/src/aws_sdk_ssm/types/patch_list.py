"""Generated from Smithy shape ``com.amazonaws.ssm#PatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch

PatchList: TypeAlias = list["aws_sdk_ssm.types.patch.Patch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchList) -> list:
    import aws_sdk_ssm.types.patch

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.patch.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchList:
    import aws_sdk_ssm.types.patch

    out: PatchList = []
    for item in data:
        out.append(aws_sdk_ssm.types.patch.deserialize_aws_json_1_1(item))
    return out
