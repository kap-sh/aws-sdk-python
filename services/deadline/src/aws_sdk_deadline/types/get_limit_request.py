"""Generated from Smithy shape ``com.amazonaws.deadline#GetLimitRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id


class GetLimitRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the limit.</p>"""
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLimitRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLimitRequest:
    out: GetLimitRequest = {}  # type: ignore[typeddict-item]
    return out
