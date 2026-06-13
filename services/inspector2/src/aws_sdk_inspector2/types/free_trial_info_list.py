"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.free_trial_info

FreeTrialInfoList: TypeAlias = list[
    "aws_sdk_inspector2.types.free_trial_info.FreeTrialInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialInfoList) -> list:
    import aws_sdk_inspector2.types.free_trial_info

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.free_trial_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeTrialInfoList:
    import aws_sdk_inspector2.types.free_trial_info

    out: FreeTrialInfoList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.free_trial_info.deserialize_json(item))
    return out
