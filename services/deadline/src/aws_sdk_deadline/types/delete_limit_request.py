"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id


class DeleteLimitRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the limit to delete.</p>"""
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLimitRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLimitRequest:
    out: DeleteLimitRequest = {}  # type: ignore[typeddict-item]
    return out
