"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialAccountInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.free_trial_account_info

FreeTrialAccountInfoList: TypeAlias = list[
    "aws_sdk_inspector2.types.free_trial_account_info.FreeTrialAccountInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialAccountInfoList) -> list:
    import aws_sdk_inspector2.types.free_trial_account_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.free_trial_account_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FreeTrialAccountInfoList:
    import aws_sdk_inspector2.types.free_trial_account_info

    out: FreeTrialAccountInfoList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.free_trial_account_info.deserialize_json(item)
        )
    return out
