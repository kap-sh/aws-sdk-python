"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_detail

QuotaShareList: TypeAlias = list[
    "aws_sdk_batch.types.quota_share_detail.QuotaShareDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareList) -> list:
    import aws_sdk_batch.types.quota_share_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.quota_share_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuotaShareList:
    import aws_sdk_batch.types.quota_share_detail

    out: QuotaShareList = []
    for item in data:
        out.append(aws_sdk_batch.types.quota_share_detail.deserialize_json(item))
    return out
