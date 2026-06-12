"""Generated from Smithy shape ``com.amazonaws.ssm#EffectivePatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.effective_patch

EffectivePatchList: TypeAlias = list["aws_sdk_ssm.types.effective_patch.EffectivePatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePatchList) -> list:
    import aws_sdk_ssm.types.effective_patch

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.effective_patch.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EffectivePatchList:
    import aws_sdk_ssm.types.effective_patch

    out: EffectivePatchList = []
    for item in data:
        out.append(aws_sdk_ssm.types.effective_patch.deserialize_aws_json_1_1(item))
    return out
