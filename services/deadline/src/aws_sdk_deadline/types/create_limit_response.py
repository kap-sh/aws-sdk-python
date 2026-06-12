"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLimitResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.limit_id


class CreateLimitResponse(TypedDict):
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>A unique identifier for the limit. Use this identifier in other operations, such as <code>CreateQueueLimitAssociation</code> and <code>DeleteLimit</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLimitResponse) -> dict:
    out: dict = {}
    out["limitId"] = value["limit_id"]
    return out


def deserialize_json(data: dict) -> CreateLimitResponse:
    out: CreateLimitResponse = {}  # type: ignore[typeddict-item]
    if "limitId" in data:
        out["limit_id"] = data["limitId"]
    else:
        raise DeserializationError("CreateLimitResponse.limit_id required")
    return out
