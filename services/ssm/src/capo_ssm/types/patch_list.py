"""Generated from Smithy shape ``com.amazonaws.ssm#PatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch

PatchList: TypeAlias = list["capo_ssm.types.patch.Patch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchList) -> list:
    import capo_ssm.types.patch

    out: list = []
    for item in value:
        out.append(capo_ssm.types.patch.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchList:
    import capo_ssm.types.patch

    out: PatchList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.patch.deserialize_aws_json_1_1(item))
    return out
