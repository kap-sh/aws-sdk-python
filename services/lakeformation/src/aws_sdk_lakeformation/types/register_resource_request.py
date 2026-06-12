"""Generated from Smithy shape ``com.amazonaws.lakeformation#RegisterResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.account_id_string
    import aws_sdk_lakeformation.types.boolean
    import aws_sdk_lakeformation.types.iam_role_arn
    import aws_sdk_lakeformation.types.nullable_boolean
    import aws_sdk_lakeformation.types.resource_arn_string


class RegisterResourceRequest(TypedDict):
    resource_arn: "aws_sdk_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to register.</p>"""
    use_service_linked_role: NotRequired[
        "aws_sdk_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Designates an Identity and Access Management (IAM) service-linked role by registering this role with the Data Catalog. A service-linked role is a unique type of IAM role that is linked directly to Lake Formation.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-roles.html\">Using Service-Linked Roles for Lake Formation</a>.</p>"""
    role_arn: NotRequired["aws_sdk_lakeformation.types.iam_role_arn.IAMRoleArn"]
    """<p>The identifier for the role that registers the resource.</p>"""
    with_federation: NotRequired[
        "aws_sdk_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether or not the resource is a federated resource.</p>"""
    hybrid_access_enabled: NotRequired[
        "aws_sdk_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies. </p>"""
    with_privileged_access: "aws_sdk_lakeformation.types.boolean.Boolean"
    """<p>Grants the calling principal the permissions to perform all supported Lake Formation operations on the registered data location. </p>"""
    expected_resource_owner_account: NotRequired[
        "aws_sdk_lakeformation.types.account_id_string.AccountIdString"
    ]
    """<p>The Amazon Web Services account that owns the Glue tables associated with specific Amazon S3 locations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "use_service_linked_role" in value:
        out["UseServiceLinkedRole"] = value["use_service_linked_role"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "with_federation" in value:
        out["WithFederation"] = value["with_federation"]
    if "hybrid_access_enabled" in value:
        out["HybridAccessEnabled"] = value["hybrid_access_enabled"]
    out["WithPrivilegedAccess"] = value.get("with_privileged_access", False)
    if "expected_resource_owner_account" in value:
        out["ExpectedResourceOwnerAccount"] = value["expected_resource_owner_account"]
    return out


def deserialize_json(data: dict) -> RegisterResourceRequest:
    out: RegisterResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("RegisterResourceRequest.resource_arn required")
    if "UseServiceLinkedRole" in data:
        out["use_service_linked_role"] = data["UseServiceLinkedRole"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "WithFederation" in data:
        out["with_federation"] = data["WithFederation"]
    if "HybridAccessEnabled" in data:
        out["hybrid_access_enabled"] = data["HybridAccessEnabled"]
    if "WithPrivilegedAccess" in data:
        out["with_privileged_access"] = data["WithPrivilegedAccess"]
    else:
        out["with_privileged_access"] = False
    if "ExpectedResourceOwnerAccount" in data:
        out["expected_resource_owner_account"] = data["ExpectedResourceOwnerAccount"]
    return out
