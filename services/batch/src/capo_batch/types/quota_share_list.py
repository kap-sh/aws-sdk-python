"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.quota_share_detail

QuotaShareList: TypeAlias = list["capo_batch.types.quota_share_detail.QuotaShareDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareList) -> list:
    import capo_batch.types.quota_share_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.quota_share_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuotaShareList:
    import capo_batch.types.quota_share_detail

    out: QuotaShareList = []
    for item in data:
        out.append(capo_batch.types.quota_share_detail.deserialize_json(item))
    return out
