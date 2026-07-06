"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseConversionTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.date_time
    import aws_sdk_license_manager.types.license_conversion_context
    import aws_sdk_license_manager.types.license_conversion_task_id
    import aws_sdk_license_manager.types.license_conversion_task_status
    import aws_sdk_license_manager.types.string


class GetLicenseConversionTaskResponse(TypedDict, closed=True):
    license_conversion_task_id: NotRequired[
        "aws_sdk_license_manager.types.license_conversion_task_id.LicenseConversionTaskId"
    ]
    """<p>ID of the license type conversion task.</p>"""
    resource_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Names (ARN) of the resources the license conversion task is associated with.</p>"""
    source_license_context: NotRequired[
        "aws_sdk_license_manager.types.license_conversion_context.LicenseConversionContext"
    ]
    """<p>Information about the license type converted from.</p>"""
    destination_license_context: NotRequired[
        "aws_sdk_license_manager.types.license_conversion_context.LicenseConversionContext"
    ]
    """<p>Information about the license type converted to.</p>"""
    status_message: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>The status message for the conversion task.</p>"""
    status: NotRequired[
        "aws_sdk_license_manager.types.license_conversion_task_status.LicenseConversionTaskStatus"
    ]
    """<p>Status of the license type conversion task.</p>"""
    start_time: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>Time at which the license type conversion task was started .</p>"""
    license_conversion_time: NotRequired[
        "aws_sdk_license_manager.types.date_time.DateTime"
    ]
    """<p>Amount of time to complete the license type conversion.</p>"""
    end_time: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>Time at which the license type conversion task was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseConversionTaskResponse) -> dict:
    out: dict = {}
    if "license_conversion_task_id" in value:
        out["LicenseConversionTaskId"] = value["license_conversion_task_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "source_license_context" in value:
        import aws_sdk_license_manager.types.license_conversion_context

        out["SourceLicenseContext"] = (
            aws_sdk_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
                value["source_license_context"]
            )
        )
    if "destination_license_context" in value:
        import aws_sdk_license_manager.types.license_conversion_context

        out["DestinationLicenseContext"] = (
            aws_sdk_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
                value["destination_license_context"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "status" in value:
        import aws_sdk_license_manager.types.license_conversion_task_status

        out["Status"] = (
            aws_sdk_license_manager.types.license_conversion_task_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["StartTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "license_conversion_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["LicenseConversionTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["license_conversion_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["EndTime"] = aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseConversionTaskResponse:
    out: GetLicenseConversionTaskResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConversionTaskId" in data:
        out["license_conversion_task_id"] = data["LicenseConversionTaskId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "SourceLicenseContext" in data:
        import aws_sdk_license_manager.types.license_conversion_context

        out["source_license_context"] = (
            aws_sdk_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["SourceLicenseContext"]
            )
        )
    if "DestinationLicenseContext" in data:
        import aws_sdk_license_manager.types.license_conversion_context

        out["destination_license_context"] = (
            aws_sdk_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["DestinationLicenseContext"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "Status" in data:
        import aws_sdk_license_manager.types.license_conversion_task_status

        out["status"] = (
            aws_sdk_license_manager.types.license_conversion_task_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["start_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "LicenseConversionTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["license_conversion_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LicenseConversionTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["end_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    return out
