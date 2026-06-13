"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupStatusDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.error_detail
    import aws_sdk_qbusiness.types.group_status
    import aws_sdk_qbusiness.types.timestamp


class GroupStatusDetail(TypedDict):
    status: NotRequired["aws_sdk_qbusiness.types.group_status.GroupStatus"]
    """<p>The status of a group.</p>"""
    last_updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated.</p>"""
    error_detail: NotRequired["aws_sdk_qbusiness.types.error_detail.ErrorDetail"]
    """<p>The details of an error associated a group status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupStatusDetail) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_qbusiness.types.group_status

        out["status"] = aws_sdk_qbusiness.types.group_status.serialize_json(
            value["status"]
        )
    if "last_updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "error_detail" in value:
        import aws_sdk_qbusiness.types.error_detail

        out["errorDetail"] = aws_sdk_qbusiness.types.error_detail.serialize_json(
            value["error_detail"]
        )
    return out


def deserialize_json(data: dict) -> GroupStatusDetail:
    out: GroupStatusDetail = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_qbusiness.types.group_status

        out["status"] = aws_sdk_qbusiness.types.group_status.deserialize_json(
            data["status"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["last_updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "errorDetail" in data:
        import aws_sdk_qbusiness.types.error_detail

        out["error_detail"] = aws_sdk_qbusiness.types.error_detail.deserialize_json(
            data["errorDetail"]
        )
    return out
