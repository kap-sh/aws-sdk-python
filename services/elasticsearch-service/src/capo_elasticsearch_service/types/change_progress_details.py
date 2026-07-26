"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ChangeProgressDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.config_change_status
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.initiated_by
    import capo_elasticsearch_service.types.message
    import capo_elasticsearch_service.types.update_timestamp


class ChangeProgressDetails(TypedDict, closed=True):
    change_id: NotRequired["capo_elasticsearch_service.types.guid.GUID"]
    """<p>The unique change identifier associated with a specific domain configuration change.</p>"""
    message: NotRequired["capo_elasticsearch_service.types.message.Message"]
    """<p>Contains an optional message associated with the domain configuration change.</p>"""
    config_change_status: NotRequired[
        "capo_elasticsearch_service.types.config_change_status.ConfigChangeStatus"
    ]
    """<p>The current status of the configuration change.</p>"""
    start_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The time that the configuration change was initiated, in Universal Coordinated Time (UTC).</p>"""
    last_updated_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The last time that the configuration change was updated.</p>"""
    initiated_by: NotRequired[
        "capo_elasticsearch_service.types.initiated_by.InitiatedBy"
    ]
    """<p>The IAM principal who initiated the configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressDetails) -> dict:
    out: dict = {}
    if "change_id" in value:
        out["ChangeId"] = value["change_id"]
    if "message" in value:
        out["Message"] = value["message"]
    if "config_change_status" in value:
        import capo_elasticsearch_service.types.config_change_status

        out["ConfigChangeStatus"] = (
            capo_elasticsearch_service.types.config_change_status.serialize_json(
                value["config_change_status"]
            )
        )
    if "start_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["StartTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "last_updated_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["LastUpdatedTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "initiated_by" in value:
        import capo_elasticsearch_service.types.initiated_by

        out["InitiatedBy"] = (
            capo_elasticsearch_service.types.initiated_by.serialize_json(
                value["initiated_by"]
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
        import capo_elasticsearch_service.types.config_change_status

        out["config_change_status"] = (
            capo_elasticsearch_service.types.config_change_status.deserialize_json(
                data["ConfigChangeStatus"]
            )
        )
    if "StartTime" in data:
        import capo_elasticsearch_service.types.update_timestamp

        out["start_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import capo_elasticsearch_service.types.update_timestamp

        out["last_updated_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if "InitiatedBy" in data:
        import capo_elasticsearch_service.types.initiated_by

        out["initiated_by"] = (
            capo_elasticsearch_service.types.initiated_by.deserialize_json(
                data["InitiatedBy"]
            )
        )
    return out
