"""Generated from Smithy shape ``com.amazonaws.opensearch#ChangeProgressStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.change_progress_stage_list
    import aws_sdk_opensearch.types.config_change_status
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.initiated_by
    import aws_sdk_opensearch.types.overall_change_status
    import aws_sdk_opensearch.types.string_list
    import aws_sdk_opensearch.types.total_number_of_stages
    import aws_sdk_opensearch.types.update_timestamp


class ChangeProgressStatusDetails(TypedDict):
    change_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The unique change identifier associated with a specific domain configuration change.</p>"""
    start_time: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the configuration change is made on the domain.</p>"""
    status: NotRequired[
        "aws_sdk_opensearch.types.overall_change_status.OverallChangeStatus"
    ]
    """<p>The overall status of the domain configuration change.</p>"""
    pending_properties: NotRequired["aws_sdk_opensearch.types.string_list.StringList"]
    """<p>The list of properties in the domain configuration change that are still pending.</p>"""
    completed_properties: NotRequired["aws_sdk_opensearch.types.string_list.StringList"]
    """<p>The list of properties in the domain configuration change that have completed.</p>"""
    total_number_of_stages: (
        "aws_sdk_opensearch.types.total_number_of_stages.TotalNumberOfStages"
    )
    """<p>The total number of stages required for the configuration change.</p>"""
    change_progress_stages: NotRequired[
        "aws_sdk_opensearch.types.change_progress_stage_list.ChangeProgressStageList"
    ]
    """<p>The specific stages that the domain is going through to perform the configuration change.</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The last time that the status of the configuration change was updated.</p>"""
    config_change_status: NotRequired[
        "aws_sdk_opensearch.types.config_change_status.ConfigChangeStatus"
    ]
    """<p>The current status of the configuration change.</p>"""
    initiated_by: NotRequired["aws_sdk_opensearch.types.initiated_by.InitiatedBy"]
    """<p>The IAM principal who initiated the configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStatusDetails) -> dict:
    out: dict = {}
    if "change_id" in value:
        out["ChangeId"] = value["change_id"]
    if "start_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["StartTime"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
            value["start_time"]
        )
    if "status" in value:
        import aws_sdk_opensearch.types.overall_change_status

        out["Status"] = aws_sdk_opensearch.types.overall_change_status.serialize_json(
            value["status"]
        )
    if "pending_properties" in value:
        import aws_sdk_opensearch.types.string_list

        out["PendingProperties"] = aws_sdk_opensearch.types.string_list.serialize_json(
            value["pending_properties"]
        )
    if "completed_properties" in value:
        import aws_sdk_opensearch.types.string_list

        out["CompletedProperties"] = (
            aws_sdk_opensearch.types.string_list.serialize_json(
                value["completed_properties"]
            )
        )
    out["TotalNumberOfStages"] = value.get("total_number_of_stages", 0)
    if "change_progress_stages" in value:
        import aws_sdk_opensearch.types.change_progress_stage_list

        out["ChangeProgressStages"] = (
            aws_sdk_opensearch.types.change_progress_stage_list.serialize_json(
                value["change_progress_stages"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_opensearch.types.update_timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
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
    return out


def deserialize_json(data: dict) -> ChangeProgressStatusDetails:
    out: ChangeProgressStatusDetails = {}  # type: ignore[typeddict-item]
    if "ChangeId" in data:
        out["change_id"] = data["ChangeId"]
    if "StartTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["start_time"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["StartTime"]
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.overall_change_status

        out["status"] = aws_sdk_opensearch.types.overall_change_status.deserialize_json(
            data["Status"]
        )
    if "PendingProperties" in data:
        import aws_sdk_opensearch.types.string_list

        out["pending_properties"] = (
            aws_sdk_opensearch.types.string_list.deserialize_json(
                data["PendingProperties"]
            )
        )
    if "CompletedProperties" in data:
        import aws_sdk_opensearch.types.string_list

        out["completed_properties"] = (
            aws_sdk_opensearch.types.string_list.deserialize_json(
                data["CompletedProperties"]
            )
        )
    if "TotalNumberOfStages" in data:
        out["total_number_of_stages"] = data["TotalNumberOfStages"]
    else:
        out["total_number_of_stages"] = 0
    if "ChangeProgressStages" in data:
        import aws_sdk_opensearch.types.change_progress_stage_list

        out["change_progress_stages"] = (
            aws_sdk_opensearch.types.change_progress_stage_list.deserialize_json(
                data["ChangeProgressStages"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["last_updated_time"] = (
            aws_sdk_opensearch.types.update_timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
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
    return out
