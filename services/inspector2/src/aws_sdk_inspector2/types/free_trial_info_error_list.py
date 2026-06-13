"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialInfoErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.free_trial_info_error

FreeTrialInfoErrorList: TypeAlias = list[
    "aws_sdk_inspector2.types.free_trial_info_error.FreeTrialInfoError"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialInfoErrorList) -> list:
    import aws_sdk_inspector2.types.free_trial_info_error

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.free_trial_info_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeTrialInfoErrorList:
    import aws_sdk_inspector2.types.free_trial_info_error

    out: FreeTrialInfoErrorList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.free_trial_info_error.deserialize_json(item)
        )
    return out
