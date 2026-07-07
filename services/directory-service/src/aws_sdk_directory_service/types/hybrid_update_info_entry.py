"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateInfoEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_id
    import aws_sdk_directory_service.types.hybrid_update_value
    import aws_sdk_directory_service.types.initiated_by
    import aws_sdk_directory_service.types.last_updated_date_time
    import aws_sdk_directory_service.types.start_date_time
    import aws_sdk_directory_service.types.update_status
    import aws_sdk_directory_service.types.update_status_reason


class HybridUpdateInfoEntry(TypedDict, closed=True):
    status: NotRequired["aws_sdk_directory_service.types.update_status.UpdateStatus"]
    """<p>The current status of the update activity. Valid values include <code>UPDATED</code>, <code>UPDATING</code>, and <code>UPDATE_FAILED</code>.</p>"""
    status_reason: NotRequired[
        "aws_sdk_directory_service.types.update_status_reason.UpdateStatusReason"
    ]
    """<p>A human-readable description of the update status, including any error details or progress information.</p>"""
    initiated_by: NotRequired[
        "aws_sdk_directory_service.types.initiated_by.InitiatedBy"
    ]
    """<p>Specifies if the update was initiated by the customer or Amazon Web Services.</p>"""
    new_value: NotRequired[
        "aws_sdk_directory_service.types.hybrid_update_value.HybridUpdateValue"
    ]
    """<p>The new configuration values being applied in this update.</p>"""
    previous_value: NotRequired[
        "aws_sdk_directory_service.types.hybrid_update_value.HybridUpdateValue"
    ]
    """<p>The previous configuration values before this update was applied.</p>"""
    start_time: NotRequired[
        "aws_sdk_directory_service.types.start_date_time.StartDateTime"
    ]
    """<p>The date and time when the update activity was initiated.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the update activity status was last updated.</p>"""
    assessment_id: NotRequired[
        "aws_sdk_directory_service.types.assessment_id.AssessmentId"
    ]
    """<p>The identifier of the assessment performed to validate this update configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateInfoEntry) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_directory_service.types.update_status

        out["Status"] = (
            aws_sdk_directory_service.types.update_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "initiated_by" in value:
        out["InitiatedBy"] = value["initiated_by"]
    if "new_value" in value:
        import aws_sdk_directory_service.types.hybrid_update_value

        out["NewValue"] = (
            aws_sdk_directory_service.types.hybrid_update_value.serialize_aws_json_1_1(
                value["new_value"]
            )
        )
    if "previous_value" in value:
        import aws_sdk_directory_service.types.hybrid_update_value

        out["PreviousValue"] = (
            aws_sdk_directory_service.types.hybrid_update_value.serialize_aws_json_1_1(
                value["previous_value"]
            )
        )
    if "start_time" in value:
        import aws_sdk_directory_service.types.start_date_time

        out["StartTime"] = (
            aws_sdk_directory_service.types.start_date_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "last_updated_date_time" in value:
        import aws_sdk_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            aws_sdk_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridUpdateInfoEntry:
    out: HybridUpdateInfoEntry = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_directory_service.types.update_status

        out["status"] = (
            aws_sdk_directory_service.types.update_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "InitiatedBy" in data:
        out["initiated_by"] = data["InitiatedBy"]
    if "NewValue" in data:
        import aws_sdk_directory_service.types.hybrid_update_value

        out["new_value"] = (
            aws_sdk_directory_service.types.hybrid_update_value.deserialize_aws_json_1_1(
                data["NewValue"]
            )
        )
    if "PreviousValue" in data:
        import aws_sdk_directory_service.types.hybrid_update_value

        out["previous_value"] = (
            aws_sdk_directory_service.types.hybrid_update_value.deserialize_aws_json_1_1(
                data["PreviousValue"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_directory_service.types.start_date_time

        out["start_time"] = (
            aws_sdk_directory_service.types.start_date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "LastUpdatedDateTime" in data:
        import aws_sdk_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            aws_sdk_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    if "AssessmentId" in data:
        out["assessment_id"] = data["AssessmentId"]
    return out
