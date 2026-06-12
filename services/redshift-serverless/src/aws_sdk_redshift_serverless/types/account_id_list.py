"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#AccountIdList``."""

from typing import TypeAlias

AccountIdList: TypeAlias = list["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountIdList:
    return list(data)