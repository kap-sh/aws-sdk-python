"""Generated from Smithy shape ``com.amazonaws.ssm#PatchFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_filter_value

PatchFilterValueList: TypeAlias = list[
    "capo_ssm.types.patch_filter_value.PatchFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchFilterValueList:
    return list(data)
