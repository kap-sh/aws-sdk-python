"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ErrorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.account_id
    import aws_sdk_migration_hub_refactor_spaces.types.additional_details
    import aws_sdk_migration_hub_refactor_spaces.types.error_code
    import aws_sdk_migration_hub_refactor_spaces.types.error_message
    import aws_sdk_migration_hub_refactor_spaces.types.error_resource_type
    import aws_sdk_migration_hub_refactor_spaces.types.resource_identifier


class ErrorResponse(TypedDict):
    code: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.error_code.ErrorCode"
    ]
    """<p>The error code associated with the error. </p>"""
    message: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.error_message.ErrorMessage"
    ]
    """<p>The message associated with the error. </p>"""
    account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the resource owner. </p>"""
    resource_identifier: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The ID of the resource. </p>"""
    resource_type: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.error_resource_type.ErrorResourceType"
    ]
    """<p>The type of resource. </p>"""
    additional_details: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.additional_details.AdditionalDetails"
    ]
    """<p>Additional details about the error. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorResponse) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "additional_details" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.additional_details

        out["AdditionalDetails"] = (
            aws_sdk_migration_hub_refactor_spaces.types.additional_details.serialize_json(
                value["additional_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ErrorResponse:
    out: ErrorResponse = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "AdditionalDetails" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.additional_details

        out["additional_details"] = (
            aws_sdk_migration_hub_refactor_spaces.types.additional_details.deserialize_json(
                data["AdditionalDetails"]
            )
        )
    return out
