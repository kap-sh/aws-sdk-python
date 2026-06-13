"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_status_detail
    import aws_sdk_qbusiness.types.group_status_details


class GetGroupResponse(TypedDict):
    status: NotRequired["aws_sdk_qbusiness.types.group_status_detail.GroupStatusDetail"]
    """<p>The current status of the group.</p>"""
    status_history: NotRequired[
        "aws_sdk_qbusiness.types.group_status_details.GroupStatusDetails"
    ]
    """<p>The status history of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_qbusiness.types.group_status_detail

        out["status"] = aws_sdk_qbusiness.types.group_status_detail.serialize_json(
            value["status"]
        )
    if "status_history" in value:
        import aws_sdk_qbusiness.types.group_status_details

        out["statusHistory"] = (
            aws_sdk_qbusiness.types.group_status_details.serialize_json(
                value["status_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGroupResponse:
    out: GetGroupResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_qbusiness.types.group_status_detail

        out["status"] = aws_sdk_qbusiness.types.group_status_detail.deserialize_json(
            data["status"]
        )
    if "statusHistory" in data:
        import aws_sdk_qbusiness.types.group_status_details

        out["status_history"] = (
            aws_sdk_qbusiness.types.group_status_details.deserialize_json(
                data["statusHistory"]
            )
        )
    return out
