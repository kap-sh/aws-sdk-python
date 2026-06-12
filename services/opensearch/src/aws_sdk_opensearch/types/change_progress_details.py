"""Generated from Smithy shape ``com.amazonaws.opensearch#ChangeProgressDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.config_change_status
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.initiated_by
    import aws_sdk_opensearch.types.message
    import aws_sdk_opensearch.types.update_timestamp


class ChangeProgressDetails(TypedDict):
    change_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The ID of the configuration change.</p>"""
    message: NotRequired["aws_sdk_opensearch.types.message.Message"]
    """<p>A message corresponding to the status of the configuration change.</p>"""
    config_change_status: NotRequired[
        "aws_sdk_opensearch.types.config_change_status.ConfigChangeStatus"
    ]
    """<p>The current status of the configuration change.</p>"""
    initiated_by: NotRequired["aws_sdk_opensearch.types.initiated_by.InitiatedBy"]
    """<p>The IAM principal who initiated the configuration change.</p>"""
    start_time: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time that the configuration change was initiated, in Universal Coordinated Time (UTC).</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The last time that the configuration change was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressDetails) -> dict:
    out: dict = {}
    if "change_id" in value:
        out["ChangeId"] = value["change_id"]
    if "message" in value:
        out["Message"] = value["message"]
    if "config_change_status" in value:
        import aws_sdk_opensearch.types.config_change_status

        out["ConfigChangeStatus"] = (
            aws_sdk_opensearch.types.config_change_status.serialize_json(
                value["config_change_status"]
            )
        )
    if "initiated_by" in value:
        import aws_sdk_opensearch.types.initiated_by

        out["InitiatedBy"] = aws_sdk_opensearch.types.initiated_by.serialize_json(
            value["initiated_by"]
        )
    if "start_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["StartTime"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
            value["start_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_opensearch.types.update_timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChangeProgressDetails:
    out: ChangeProgressDetails = {}  # type: ignore[typeddict-item]
    if "ChangeId" in data:
        out["change_id"] = data["ChangeId"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ConfigChangeStatus" in data:
        import aws_sdk_opensearch.types.config_change_status

        out["config_change_status"] = (
            aws_sdk_opensearch.types.config_change_status.deserialize_json(
                data["ConfigChangeStatus"]
            )
        )
    if "InitiatedBy" in data:
        import aws_sdk_opensearch.types.initiated_by

        out["initiated_by"] = aws_sdk_opensearch.types.initiated_by.deserialize_json(
            data["InitiatedBy"]
        )
    if "StartTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["start_time"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["StartTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["last_updated_time"] = (
            aws_sdk_opensearch.types.update_timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
