"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#EbsUserIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.ebs_user_id

EbsUserIdList: TypeAlias = list["aws_sdk_accessanalyzer.types.ebs_user_id.EbsUserId"]


# --- restJson1 ser/de ---
def serialize_json(value: EbsUserIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> EbsUserIdList:
    return list(data)
