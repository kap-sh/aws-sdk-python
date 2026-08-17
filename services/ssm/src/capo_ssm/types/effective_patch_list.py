"""Generated from Smithy shape ``com.amazonaws.ssm#EffectivePatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.effective_patch

EffectivePatchList: TypeAlias = list["capo_ssm.types.effective_patch.EffectivePatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePatchList) -> list:
    import capo_ssm.types.effective_patch

    out: list = []
    for item in value:
        out.append(capo_ssm.types.effective_patch.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EffectivePatchList:
    import capo_ssm.types.effective_patch

    out: EffectivePatchList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.effective_patch.deserialize_aws_json_1_1(item))
    return out
