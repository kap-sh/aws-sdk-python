"""Generated from Smithy shape ``com.amazonaws.deadline#AcquiredLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.acquired_limit

AcquiredLimits: TypeAlias = list["aws_sdk_deadline.types.acquired_limit.AcquiredLimit"]


# --- restJson1 ser/de ---
def serialize_json(value: AcquiredLimits) -> list:
    import aws_sdk_deadline.types.acquired_limit

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.acquired_limit.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcquiredLimits:
    import aws_sdk_deadline.types.acquired_limit

    out: AcquiredLimits = []
    for item in data:
        out.append(aws_sdk_deadline.types.acquired_limit.deserialize_json(item))
    return out
