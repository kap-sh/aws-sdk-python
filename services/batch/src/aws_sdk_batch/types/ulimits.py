"""Generated from Smithy shape ``com.amazonaws.batch#Ulimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.ulimit

Ulimits: TypeAlias = list["aws_sdk_batch.types.ulimit.Ulimit"]


# --- restJson1 ser/de ---
def serialize_json(value: Ulimits) -> list:
    import aws_sdk_batch.types.ulimit

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.ulimit.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ulimits:
    import aws_sdk_batch.types.ulimit

    out: Ulimits = []
    for item in data:
        out.append(aws_sdk_batch.types.ulimit.deserialize_json(item))
    return out
