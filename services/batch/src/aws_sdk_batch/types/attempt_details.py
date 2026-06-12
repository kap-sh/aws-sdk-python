"""Generated from Smithy shape ``com.amazonaws.batch#AttemptDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.attempt_detail

AttemptDetails: TypeAlias = list["aws_sdk_batch.types.attempt_detail.AttemptDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: AttemptDetails) -> list:
    import aws_sdk_batch.types.attempt_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.attempt_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttemptDetails:
    import aws_sdk_batch.types.attempt_detail

    out: AttemptDetails = []
    for item in data:
        out.append(aws_sdk_batch.types.attempt_detail.deserialize_json(item))
    return out
