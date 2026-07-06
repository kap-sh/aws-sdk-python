"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateFileSystemAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.audit_destination_arn
    import aws_sdk_storage_gateway.types.cache_attributes
    import aws_sdk_storage_gateway.types.domain_user_name
    import aws_sdk_storage_gateway.types.domain_user_password
    import aws_sdk_storage_gateway.types.file_system_association_arn


class UpdateFileSystemAssociationInput(TypedDict, closed=True):
    file_system_association_arn: "aws_sdk_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    """<p>The Amazon Resource Name (ARN) of the file system association that you want to update.</p>"""
    user_name: NotRequired[
        "aws_sdk_storage_gateway.types.domain_user_name.DomainUserName"
    ]
    """<p>The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.</p>"""
    password: NotRequired[
        "aws_sdk_storage_gateway.types.domain_user_password.DomainUserPassword"
    ]
    """<p>The password of the user credential.</p>"""
    audit_destination_arn: NotRequired[
        "aws_sdk_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the storage used for the audit logs.</p>"""
    cache_attributes: NotRequired[
        "aws_sdk_storage_gateway.types.cache_attributes.CacheAttributes"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemAssociationInput) -> dict:
    out: dict = {}
    out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "audit_destination_arn" in value:
        out["AuditDestinationARN"] = value["audit_destination_arn"]
    if "cache_attributes" in value:
        import aws_sdk_storage_gateway.types.cache_attributes

        out["CacheAttributes"] = (
            aws_sdk_storage_gateway.types.cache_attributes.serialize_aws_json_1_1(
                value["cache_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemAssociationInput:
    out: UpdateFileSystemAssociationInput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationARN" in data:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    else:
        raise DeserializationError(
            "UpdateFileSystemAssociationInput.file_system_association_arn required"
        )
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "AuditDestinationARN" in data:
        out["audit_destination_arn"] = data["AuditDestinationARN"]
    if "CacheAttributes" in data:
        import aws_sdk_storage_gateway.types.cache_attributes

        out["cache_attributes"] = (
            aws_sdk_storage_gateway.types.cache_attributes.deserialize_aws_json_1_1(
                data["CacheAttributes"]
            )
        )
    return out
