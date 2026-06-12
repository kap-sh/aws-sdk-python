"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateInfoEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.initiated_by
    import aws_sdk_directory_service.types.last_updated_date_time
    import aws_sdk_directory_service.types.region_name
    import aws_sdk_directory_service.types.start_date_time
    import aws_sdk_directory_service.types.update_status
    import aws_sdk_directory_service.types.update_status_reason
    import aws_sdk_directory_service.types.update_value


class UpdateInfoEntry(TypedDict):
    region: NotRequired["aws_sdk_directory_service.types.region_name.RegionName"]
    """<p> The name of the Region. </p>"""
    status: NotRequired["aws_sdk_directory_service.types.update_status.UpdateStatus"]
    """<p> The status of the update performed on the directory. </p>"""
    status_reason: NotRequired[
        "aws_sdk_directory_service.types.update_status_reason.UpdateStatusReason"
    ]
    """<p> The reason for the current status of the update type activity. </p>"""
    initiated_by: NotRequired[
        "aws_sdk_directory_service.types.initiated_by.InitiatedBy"
    ]
    """<p> This specifies if the update was initiated by the customer or by the service team. </p>"""
    new_value: NotRequired["aws_sdk_directory_service.types.update_value.UpdateValue"]
    """<p> The new value of the target setting. </p>"""
    previous_value: NotRequired[
        "aws_sdk_directory_service.types.update_value.UpdateValue"
    ]
    """<p> The old value of the target setting. </p>"""
    start_time: NotRequired[
        "aws_sdk_directory_service.types.start_date_time.StartDateTime"
    ]
    """<p> The start time of the <code>UpdateDirectorySetup</code> for the particular type. </p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p> The last updated date and time of a particular directory setting. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInfoEntry) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
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
        import aws_sdk_directory_service.types.update_value

        out["NewValue"] = (
            aws_sdk_directory_service.types.update_value.serialize_aws_json_1_1(
                value["new_value"]
            )
        )
    if "previous_value" in value:
        import aws_sdk_directory_service.types.update_value

        out["PreviousValue"] = (
            aws_sdk_directory_service.types.update_value.serialize_aws_json_1_1(
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInfoEntry:
    out: UpdateInfoEntry = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
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
        import aws_sdk_directory_service.types.update_value

        out["new_value"] = (
            aws_sdk_directory_service.types.update_value.deserialize_aws_json_1_1(
                data["NewValue"]
            )
        )
    if "PreviousValue" in data:
        import aws_sdk_directory_service.types.update_value

        out["previous_value"] = (
            aws_sdk_directory_service.types.update_value.deserialize_aws_json_1_1(
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
    return out
