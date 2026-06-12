"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.account_id_string
    import aws_sdk_lakeformation.types.iam_role_arn
    import aws_sdk_lakeformation.types.last_modified_timestamp
    import aws_sdk_lakeformation.types.nullable_boolean
    import aws_sdk_lakeformation.types.resource_arn_string
    import aws_sdk_lakeformation.types.verification_status


class ResourceInfo(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_lakeformation.types.resource_arn_string.ResourceArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    role_arn: NotRequired["aws_sdk_lakeformation.types.iam_role_arn.IAMRoleArn"]
    """<p>The IAM role that registered a resource.</p>"""
    last_modified: NotRequired[
        "aws_sdk_lakeformation.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p>The date and time the resource was last modified.</p>"""
    with_federation: NotRequired[
        "aws_sdk_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether or not the resource is a federated resource.</p>"""
    hybrid_access_enabled: NotRequired[
        "aws_sdk_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Indicates whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies. </p>"""
    with_privileged_access: NotRequired[
        "aws_sdk_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Grants the calling principal the permissions to perform all supported Lake Formation operations on the registered data location. </p>"""
    verification_status: NotRequired[
        "aws_sdk_lakeformation.types.verification_status.VerificationStatus"
    ]
    """<p>Indicates whether the registered role has sufficient permissions to access registered Amazon S3 location. Verification Status can be one of the following: </p> <ul> <li> <p>VERIFIED - Registered role has sufficient permissions to access registered Amazon S3 location.</p> </li> <li> <p>NOT_VERIFIED - Registered role does not have sufficient permissions to access registered Amazon S3 location.</p> </li> <li> <p>VERIFICATION_FAILED - Unable to verify if the registered role can access the registered Amazon S3 location.</p> </li> </ul>"""
    expected_resource_owner_account: NotRequired[
        "aws_sdk_lakeformation.types.account_id_string.AccountIdString"
    ]
    """<p>The Amazon Web Services account that owns the Glue tables associated with specific Amazon S3 locations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInfo) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "last_modified" in value:
        import aws_sdk_lakeformation.types.last_modified_timestamp

        out["LastModified"] = (
            aws_sdk_lakeformation.types.last_modified_timestamp.serialize_json(
                value["last_modified"]
            )
        )
    if "with_federation" in value:
        out["WithFederation"] = value["with_federation"]
    if "hybrid_access_enabled" in value:
        out["HybridAccessEnabled"] = value["hybrid_access_enabled"]
    if "with_privileged_access" in value:
        out["WithPrivilegedAccess"] = value["with_privileged_access"]
    if "verification_status" in value:
        import aws_sdk_lakeformation.types.verification_status

        out["VerificationStatus"] = (
            aws_sdk_lakeformation.types.verification_status.serialize_json(
                value["verification_status"]
            )
        )
    if "expected_resource_owner_account" in value:
        out["ExpectedResourceOwnerAccount"] = value["expected_resource_owner_account"]
    return out


def deserialize_json(data: dict) -> ResourceInfo:
    out: ResourceInfo = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "LastModified" in data:
        import aws_sdk_lakeformation.types.last_modified_timestamp

        out["last_modified"] = (
            aws_sdk_lakeformation.types.last_modified_timestamp.deserialize_json(
                data["LastModified"]
            )
        )
    if "WithFederation" in data:
        out["with_federation"] = data["WithFederation"]
    if "HybridAccessEnabled" in data:
        out["hybrid_access_enabled"] = data["HybridAccessEnabled"]
    if "WithPrivilegedAccess" in data:
        out["with_privileged_access"] = data["WithPrivilegedAccess"]
    if "VerificationStatus" in data:
        import aws_sdk_lakeformation.types.verification_status

        out["verification_status"] = (
            aws_sdk_lakeformation.types.verification_status.deserialize_json(
                data["VerificationStatus"]
            )
        )
    if "ExpectedResourceOwnerAccount" in data:
        out["expected_resource_owner_account"] = data["ExpectedResourceOwnerAccount"]
    return out
