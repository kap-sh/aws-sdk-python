"""Generated from Smithy shape ``com.amazonaws.batch#TmpfsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.tmpfs

TmpfsList: TypeAlias = list["aws_sdk_batch.types.tmpfs.Tmpfs"]


# --- restJson1 ser/de ---
def serialize_json(value: TmpfsList) -> list:
    import aws_sdk_batch.types.tmpfs

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.tmpfs.serialize_json(item))
    return out


def deserialize_json(data: list) -> TmpfsList:
    import aws_sdk_batch.types.tmpfs

    out: TmpfsList = []
    for item in data:
        out.append(aws_sdk_batch.types.tmpfs.deserialize_json(item))
    return out
