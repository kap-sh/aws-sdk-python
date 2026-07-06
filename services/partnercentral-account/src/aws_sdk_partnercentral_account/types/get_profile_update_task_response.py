"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetProfileUpdateTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.date_time
    import aws_sdk_partnercentral_account.types.error_detail_list
    import aws_sdk_partnercentral_account.types.partner_arn
    import aws_sdk_partnercentral_account.types.partner_id
    import aws_sdk_partnercentral_account.types.profile_task_id
    import aws_sdk_partnercentral_account.types.profile_task_status
    import aws_sdk_partnercentral_account.types.task_details


class GetProfileUpdateTaskResponse(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "aws_sdk_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the profile update task.</p>"""
    id: "aws_sdk_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    task_id: "aws_sdk_partnercentral_account.types.profile_task_id.ProfileTaskId"
    """<p>The unique identifier of the profile update task.</p>"""
    task_details: "aws_sdk_partnercentral_account.types.task_details.TaskDetails"
    """<p>The details of the profile update task including what changes are being made.</p>"""
    started_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the profile update task was started.</p>"""
    status: "aws_sdk_partnercentral_account.types.profile_task_status.ProfileTaskStatus"
    """<p>The current status of the profile update task (in progress, completed, failed, etc.).</p>"""
    ended_at: NotRequired["aws_sdk_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the profile update task was completed or failed.</p>"""
    error_detail_list: NotRequired[
        "aws_sdk_partnercentral_account.types.error_detail_list.ErrorDetailList"
    ]
    """<p>A list of error details if any errors occurred during the profile update task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileUpdateTaskResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    out["TaskId"] = value["task_id"]
    import aws_sdk_partnercentral_account.types.task_details

    out["TaskDetails"] = (
        aws_sdk_partnercentral_account.types.task_details.serialize_aws_json_1_0(
            value["task_details"]
        )
    )
    import aws_sdk_partnercentral_account.types.date_time

    out["StartedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    import aws_sdk_partnercentral_account.types.profile_task_status

    out["Status"] = (
        aws_sdk_partnercentral_account.types.profile_task_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "ended_at" in value:
        import aws_sdk_partnercentral_account.types.date_time

        out["EndedAt"] = (
            aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["ended_at"]
            )
        )
    if "error_detail_list" in value:
        import aws_sdk_partnercentral_account.types.error_detail_list

        out["ErrorDetailList"] = (
            aws_sdk_partnercentral_account.types.error_detail_list.serialize_aws_json_1_0(
                value["error_detail_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProfileUpdateTaskResponse:
    out: GetProfileUpdateTaskResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.arn required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.id required")
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.task_id required")
    if "TaskDetails" in data:
        import aws_sdk_partnercentral_account.types.task_details

        out["task_details"] = (
            aws_sdk_partnercentral_account.types.task_details.deserialize_aws_json_1_0(
                data["TaskDetails"]
            )
        )
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.task_details required")
    if "StartedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["started_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.started_at required")
    if "Status" in data:
        import aws_sdk_partnercentral_account.types.profile_task_status

        out["status"] = (
            aws_sdk_partnercentral_account.types.profile_task_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("GetProfileUpdateTaskResponse.status required")
    if "EndedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["ended_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["EndedAt"]
            )
        )
    if "ErrorDetailList" in data:
        import aws_sdk_partnercentral_account.types.error_detail_list

        out["error_detail_list"] = (
            aws_sdk_partnercentral_account.types.error_detail_list.deserialize_aws_json_1_0(
                data["ErrorDetailList"]
            )
        )
    return out
