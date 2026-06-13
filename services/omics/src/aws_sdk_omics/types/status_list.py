"""Generated from Smithy shape ``com.amazonaws.omics#StatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.share_status

StatusList: TypeAlias = list["aws_sdk_omics.types.share_status.ShareStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: StatusList) -> list:
    return list(value)


def deserialize_json(data: list) -> StatusList:
    return list(data)
