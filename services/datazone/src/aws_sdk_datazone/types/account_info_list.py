"""Generated from Smithy shape ``com.amazonaws.datazone#AccountInfoList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_info

AccountInfoList: TypeAlias = list["aws_sdk_datazone.types.account_info.AccountInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountInfoList) -> list:
    import aws_sdk_datazone.types.account_info
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.account_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountInfoList:
    import aws_sdk_datazone.types.account_info
    out: AccountInfoList = []
    for item in data:
        out.append(aws_sdk_datazone.types.account_info.deserialize_json(item))
    return out