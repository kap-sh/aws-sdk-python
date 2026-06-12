"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseOperationFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.date_time
    import aws_sdk_license_manager.types.metadata_list
    import aws_sdk_license_manager.types.resource_type
    import aws_sdk_license_manager.types.string


class LicenseOperationFailure(TypedDict):
    resource_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_license_manager.types.resource_type.ResourceType"
    ]
    """<p>Resource type.</p>"""
    error_message: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Error message.</p>"""
    failure_time: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>Failure time.</p>"""
    operation_name: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Name of the operation.</p>"""
    resource_owner_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>ID of the Amazon Web Services account that owns the resource.</p>"""
    operation_requested_by: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>The requester is \"License Manager Automated Discovery\".</p>"""
    metadata_list: NotRequired[
        "aws_sdk_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseOperationFailure) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        import aws_sdk_license_manager.types.resource_type

        out["ResourceType"] = (
            aws_sdk_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "failure_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["FailureTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["failure_time"]
            )
        )
    if "operation_name" in value:
        out["OperationName"] = value["operation_name"]
    if "resource_owner_id" in value:
        out["ResourceOwnerId"] = value["resource_owner_id"]
    if "operation_requested_by" in value:
        out["OperationRequestedBy"] = value["operation_requested_by"]
    if "metadata_list" in value:
        import aws_sdk_license_manager.types.metadata_list

        out["MetadataList"] = (
            aws_sdk_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["metadata_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseOperationFailure:
    out: LicenseOperationFailure = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        import aws_sdk_license_manager.types.resource_type

        out["resource_type"] = (
            aws_sdk_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "FailureTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["failure_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["FailureTime"]
            )
        )
    if "OperationName" in data:
        out["operation_name"] = data["OperationName"]
    if "ResourceOwnerId" in data:
        out["resource_owner_id"] = data["ResourceOwnerId"]
    if "OperationRequestedBy" in data:
        out["operation_requested_by"] = data["OperationRequestedBy"]
    if "MetadataList" in data:
        import aws_sdk_license_manager.types.metadata_list

        out["metadata_list"] = (
            aws_sdk_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["MetadataList"]
            )
        )
    return out
