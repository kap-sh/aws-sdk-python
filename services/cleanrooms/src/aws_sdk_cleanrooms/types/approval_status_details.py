"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ApprovalStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.approval_status


class ApprovalStatusDetails(TypedDict):
    status: "aws_sdk_cleanrooms.types.approval_status.ApprovalStatus"
    """<p>The approval status of a member's vote on the change request. Valid values are PENDING (if they haven't voted), APPROVED, or DENIED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStatusDetails) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.approval_status

    out["status"] = aws_sdk_cleanrooms.types.approval_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ApprovalStatusDetails:
    out: ApprovalStatusDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_cleanrooms.types.approval_status

        out["status"] = aws_sdk_cleanrooms.types.approval_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ApprovalStatusDetails.status required")
    return out
