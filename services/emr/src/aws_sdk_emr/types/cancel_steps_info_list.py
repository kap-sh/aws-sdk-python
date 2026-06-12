"""Generated from Smithy shape ``com.amazonaws.emr#CancelStepsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.cancel_steps_info

CancelStepsInfoList: TypeAlias = list[
    "aws_sdk_emr.types.cancel_steps_info.CancelStepsInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStepsInfoList) -> list:
    import aws_sdk_emr.types.cancel_steps_info

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.cancel_steps_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CancelStepsInfoList:
    import aws_sdk_emr.types.cancel_steps_info

    out: CancelStepsInfoList = []
    for item in data:
        out.append(aws_sdk_emr.types.cancel_steps_info.deserialize_aws_json_1_1(item))
    return out
