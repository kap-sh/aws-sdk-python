"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConversionTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.date_time
    import capo_license_manager.types.license_conversion_context
    import capo_license_manager.types.license_conversion_task_id
    import capo_license_manager.types.license_conversion_task_status
    import capo_license_manager.types.string


class LicenseConversionTask(TypedDict, closed=True):
    license_conversion_task_id: NotRequired[
        "capo_license_manager.types.license_conversion_task_id.LicenseConversionTaskId"
    ]
    """<p>The ID of the license type conversion task.</p>"""
    resource_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource associated with the license type conversion task.</p>"""
    source_license_context: NotRequired[
        "capo_license_manager.types.license_conversion_context.LicenseConversionContext"
    ]
    """<p>Information about the license type this conversion task converted from.</p>"""
    destination_license_context: NotRequired[
        "capo_license_manager.types.license_conversion_context.LicenseConversionContext"
    ]
    """<p>Information about the license type this conversion task converted to.</p>"""
    status: NotRequired[
        "capo_license_manager.types.license_conversion_task_status.LicenseConversionTaskStatus"
    ]
    """<p>The status of the conversion task.</p>"""
    status_message: NotRequired["capo_license_manager.types.string.String"]
    """<p>The status message for the conversion task.</p>"""
    start_time: NotRequired["capo_license_manager.types.date_time.DateTime"]
    """<p>The time the conversion task was started at.</p>"""
    license_conversion_time: NotRequired[
        "capo_license_manager.types.date_time.DateTime"
    ]
    """<p>The time the usage operation value of the resource was changed.</p>"""
    end_time: NotRequired["capo_license_manager.types.date_time.DateTime"]
    """<p>The time the conversion task was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConversionTask) -> dict:
    out: dict = {}
    if "license_conversion_task_id" in value:
        out["LicenseConversionTaskId"] = value["license_conversion_task_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "source_license_context" in value:
        import capo_license_manager.types.license_conversion_context

        out["SourceLicenseContext"] = (
            capo_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
                value["source_license_context"]
            )
        )
    if "destination_license_context" in value:
        import capo_license_manager.types.license_conversion_context

        out["DestinationLicenseContext"] = (
            capo_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
                value["destination_license_context"]
            )
        )
    if "status" in value:
        import capo_license_manager.types.license_conversion_task_status

        out["Status"] = (
            capo_license_manager.types.license_conversion_task_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "start_time" in value:
        import capo_license_manager.types.date_time

        out["StartTime"] = capo_license_manager.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "license_conversion_time" in value:
        import capo_license_manager.types.date_time

        out["LicenseConversionTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["license_conversion_time"]
            )
        )
    if "end_time" in value:
        import capo_license_manager.types.date_time

        out["EndTime"] = capo_license_manager.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseConversionTask:
    out: LicenseConversionTask = {}  # type: ignore[typeddict-item]
    if "LicenseConversionTaskId" in data:
        out["license_conversion_task_id"] = data["LicenseConversionTaskId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "SourceLicenseContext" in data:
        import capo_license_manager.types.license_conversion_context

        out["source_license_context"] = (
            capo_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["SourceLicenseContext"]
            )
        )
    if "DestinationLicenseContext" in data:
        import capo_license_manager.types.license_conversion_context

        out["destination_license_context"] = (
            capo_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["DestinationLicenseContext"]
            )
        )
    if "Status" in data:
        import capo_license_manager.types.license_conversion_task_status

        out["status"] = (
            capo_license_manager.types.license_conversion_task_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "StartTime" in data:
        import capo_license_manager.types.date_time

        out["start_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "LicenseConversionTime" in data:
        import capo_license_manager.types.date_time

        out["license_conversion_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LicenseConversionTime"]
            )
        )
    if "EndTime" in data:
        import capo_license_manager.types.date_time

        out["end_time"] = capo_license_manager.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
