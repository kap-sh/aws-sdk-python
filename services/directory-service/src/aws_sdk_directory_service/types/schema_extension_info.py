"""Generated from Smithy shape ``com.amazonaws.directoryservice#SchemaExtensionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.description
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.end_date_time
    import aws_sdk_directory_service.types.schema_extension_id
    import aws_sdk_directory_service.types.schema_extension_status
    import aws_sdk_directory_service.types.schema_extension_status_reason
    import aws_sdk_directory_service.types.start_date_time


class SchemaExtensionInfo(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The identifier of the directory to which the schema extension is applied.</p>"""
    schema_extension_id: NotRequired[
        "aws_sdk_directory_service.types.schema_extension_id.SchemaExtensionId"
    ]
    """<p>The identifier of the schema extension.</p>"""
    description: NotRequired["aws_sdk_directory_service.types.description.Description"]
    """<p>A description of the schema extension.</p>"""
    schema_extension_status: NotRequired[
        "aws_sdk_directory_service.types.schema_extension_status.SchemaExtensionStatus"
    ]
    """<p>The current status of the schema extension.</p>"""
    schema_extension_status_reason: NotRequired[
        "aws_sdk_directory_service.types.schema_extension_status_reason.SchemaExtensionStatusReason"
    ]
    """<p>The reason for the <code>SchemaExtensionStatus</code>.</p>"""
    start_date_time: NotRequired[
        "aws_sdk_directory_service.types.start_date_time.StartDateTime"
    ]
    """<p>The date and time that the schema extension started being applied to the directory.</p>"""
    end_date_time: NotRequired[
        "aws_sdk_directory_service.types.end_date_time.EndDateTime"
    ]
    """<p>The date and time that the schema extension was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaExtensionInfo) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "schema_extension_id" in value:
        out["SchemaExtensionId"] = value["schema_extension_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "schema_extension_status" in value:
        import aws_sdk_directory_service.types.schema_extension_status

        out["SchemaExtensionStatus"] = (
            aws_sdk_directory_service.types.schema_extension_status.serialize_aws_json_1_1(
                value["schema_extension_status"]
            )
        )
    if "schema_extension_status_reason" in value:
        out["SchemaExtensionStatusReason"] = value["schema_extension_status_reason"]
    if "start_date_time" in value:
        import aws_sdk_directory_service.types.start_date_time

        out["StartDateTime"] = (
            aws_sdk_directory_service.types.start_date_time.serialize_aws_json_1_1(
                value["start_date_time"]
            )
        )
    if "end_date_time" in value:
        import aws_sdk_directory_service.types.end_date_time

        out["EndDateTime"] = (
            aws_sdk_directory_service.types.end_date_time.serialize_aws_json_1_1(
                value["end_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaExtensionInfo:
    out: SchemaExtensionInfo = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "SchemaExtensionId" in data:
        out["schema_extension_id"] = data["SchemaExtensionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SchemaExtensionStatus" in data:
        import aws_sdk_directory_service.types.schema_extension_status

        out["schema_extension_status"] = (
            aws_sdk_directory_service.types.schema_extension_status.deserialize_aws_json_1_1(
                data["SchemaExtensionStatus"]
            )
        )
    if "SchemaExtensionStatusReason" in data:
        out["schema_extension_status_reason"] = data["SchemaExtensionStatusReason"]
    if "StartDateTime" in data:
        import aws_sdk_directory_service.types.start_date_time

        out["start_date_time"] = (
            aws_sdk_directory_service.types.start_date_time.deserialize_aws_json_1_1(
                data["StartDateTime"]
            )
        )
    if "EndDateTime" in data:
        import aws_sdk_directory_service.types.end_date_time

        out["end_date_time"] = (
            aws_sdk_directory_service.types.end_date_time.deserialize_aws_json_1_1(
                data["EndDateTime"]
            )
        )
    return out
