"""Generated from Smithy shape ``com.amazonaws.ssm#AccountSharingInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.account_sharing_info

AccountSharingInfoList: TypeAlias = list[
    "capo_ssm.types.account_sharing_info.AccountSharingInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountSharingInfoList) -> list:
    import capo_ssm.types.account_sharing_info

    out: list = []
    for item in value:
        out.append(capo_ssm.types.account_sharing_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccountSharingInfoList:
    import capo_ssm.types.account_sharing_info

    out: AccountSharingInfoList = []
    for item in data:
        out.append(capo_ssm.types.account_sharing_info.deserialize_aws_json_1_1(item))
    return out
