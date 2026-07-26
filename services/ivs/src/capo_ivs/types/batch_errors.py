"""Generated from Smithy shape ``com.amazonaws.ivs#BatchErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.batch_error

BatchErrors: TypeAlias = list["capo_ivs.types.batch_error.BatchError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchErrors) -> list:
    import capo_ivs.types.batch_error

    out: list = []
    for item in value:
        out.append(capo_ivs.types.batch_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchErrors:
    import capo_ivs.types.batch_error

    out: BatchErrors = []
    for item in data:
        out.append(capo_ivs.types.batch_error.deserialize_json(item))
    return out
