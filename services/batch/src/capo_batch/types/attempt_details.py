"""Generated from Smithy shape ``com.amazonaws.batch#AttemptDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.attempt_detail

AttemptDetails: TypeAlias = list["capo_batch.types.attempt_detail.AttemptDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: AttemptDetails) -> list:
    import capo_batch.types.attempt_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.attempt_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttemptDetails:
    import capo_batch.types.attempt_detail

    out: AttemptDetails = []
    for item in data:
        out.append(capo_batch.types.attempt_detail.deserialize_json(item))
    return out
