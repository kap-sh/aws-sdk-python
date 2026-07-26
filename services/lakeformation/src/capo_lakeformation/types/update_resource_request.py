"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.account_id_string
    import capo_lakeformation.types.iam_role_arn
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.resource_arn_string


class UpdateResourceRequest(TypedDict, closed=True):
    role_arn: "capo_lakeformation.types.iam_role_arn.IAMRoleArn"
    """<p>The new role to use for the given resource registered in Lake Formation.</p>"""
    resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The resource ARN.</p>"""
    with_federation: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether or not the resource is a federated resource.</p>"""
    hybrid_access_enabled: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies. </p>"""
    expected_resource_owner_account: NotRequired[
        "capo_lakeformation.types.account_id_string.AccountIdString"
    ]
    """<p>The Amazon Web Services account that owns the Glue tables associated with specific Amazon S3 locations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceRequest) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["ResourceArn"] = value["resource_arn"]
    if "with_federation" in value:
        out["WithFederation"] = value["with_federation"]
    if "hybrid_access_enabled" in value:
        out["HybridAccessEnabled"] = value["hybrid_access_enabled"]
    if "expected_resource_owner_account" in value:
        out["ExpectedResourceOwnerAccount"] = value["expected_resource_owner_account"]
    return out


def deserialize_json(data: dict) -> UpdateResourceRequest:
    out: UpdateResourceRequest = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("UpdateResourceRequest.role_arn required")
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UpdateResourceRequest.resource_arn required")
    if "WithFederation" in data:
        out["with_federation"] = data["WithFederation"]
    if "HybridAccessEnabled" in data:
        out["hybrid_access_enabled"] = data["HybridAccessEnabled"]
    if "ExpectedResourceOwnerAccount" in data:
        out["expected_resource_owner_account"] = data["ExpectedResourceOwnerAccount"]
    return out
