"""Generated from Smithy shape ``com.amazonaws.deadline#AcquiredLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.min_one_max_integer


class AcquiredLimit(TypedDict, closed=True):
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit.</p>"""
    count: "aws_sdk_deadline.types.min_one_max_integer.MinOneMaxInteger"
    """<p>The number of limit resources used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcquiredLimit) -> dict:
    out: dict = {}
    out["limitId"] = value["limit_id"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> AcquiredLimit:
    out: AcquiredLimit = {}  # type: ignore[typeddict-item]
    if "limitId" in data:
        out["limit_id"] = data["limitId"]
    else:
        raise DeserializationError("AcquiredLimit.limit_id required")
    if "count" in data:
        out["count"] = data["count"]
    else:
        raise DeserializationError("AcquiredLimit.count required")
    return out
