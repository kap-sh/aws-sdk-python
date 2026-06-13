"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AccountInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_info

AccountInfoList: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.account_info.AccountInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountInfoList) -> list:
    import aws_sdk_compute_optimizer_automation.types.account_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.account_info.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccountInfoList:
    import aws_sdk_compute_optimizer_automation.types.account_info

    out: AccountInfoList = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.account_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
