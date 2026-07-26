"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.batch_error

BatchErrorList: TypeAlias = list["capo_repostspace.types.batch_error.BatchError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchErrorList) -> list:
    import capo_repostspace.types.batch_error

    out: list = []
    for item in value:
        out.append(capo_repostspace.types.batch_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchErrorList:
    import capo_repostspace.types.batch_error

    out: BatchErrorList = []
    for item in data:
        out.append(capo_repostspace.types.batch_error.deserialize_json(item))
    return out
