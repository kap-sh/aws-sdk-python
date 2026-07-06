"""Generated from Smithy shape ``com.amazonaws.fsx#ActiveDirectoryBackupAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.active_directory_fully_qualified_name
    import aws_sdk_fsx.types.directory_id
    import aws_sdk_fsx.types.resource_arn


class ActiveDirectoryBackupAttributes(TypedDict, closed=True):
    domain_name: NotRequired[
        "aws_sdk_fsx.types.active_directory_fully_qualified_name.ActiveDirectoryFullyQualifiedName"
    ]
    """<p>The fully qualified domain name of the self-managed Active Directory directory.</p>"""
    active_directory_id: NotRequired["aws_sdk_fsx.types.directory_id.DirectoryId"]
    """<p>The ID of the Amazon Web Services Managed Microsoft Active Directory instance to which the file system is joined.</p>"""
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveDirectoryBackupAttributes) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "active_directory_id" in value:
        out["ActiveDirectoryId"] = value["active_directory_id"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveDirectoryBackupAttributes:
    out: ActiveDirectoryBackupAttributes = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "ActiveDirectoryId" in data:
        out["active_directory_id"] = data["ActiveDirectoryId"]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    return out
