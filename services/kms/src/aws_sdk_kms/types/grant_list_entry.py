"""Generated from Smithy shape ``com.amazonaws.kms#GrantListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.grant_constraints
    import aws_sdk_kms.types.grant_id_type
    import aws_sdk_kms.types.grant_name_type
    import aws_sdk_kms.types.grant_operation_list
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.principal_id_type
    import aws_sdk_kms.types.service_principal_type


class GrantListEntry(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The unique identifier for the KMS key to which the grant applies.</p>"""
    grant_id: NotRequired["aws_sdk_kms.types.grant_id_type.GrantIdType"]
    """<p>The unique identifier for the grant.</p>"""
    name: NotRequired["aws_sdk_kms.types.grant_name_type.GrantNameType"]
    """<p>The friendly name that identifies the grant. If a name was provided in the <a>CreateGrant</a> request, that name is returned. Otherwise this value is null.</p>"""
    creation_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>The date and time when the grant was created.</p>"""
    grantee_principal: NotRequired[
        "aws_sdk_kms.types.principal_id_type.PrincipalIdType"
    ]
    """<p>The identity that gets the permissions in the grant.</p> <p>When a grant is created with the <code>GranteePrincipal</code> field, the <code>ListGrants</code> response usually contains the user or role designated as the grantee principal in the grant. However, if the grantee principal is an Amazon Web Services service, the <code>GranteePrincipal</code> field contains an Amazon Web Services <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">service principal</a>, which might correspond to several different grantee principals, such as an IAM user, IAM role, or Amazon Web Services account.</p>"""
    retiring_principal: NotRequired[
        "aws_sdk_kms.types.principal_id_type.PrincipalIdType"
    ]
    """<p>The principal that can retire the grant.</p>"""
    issuing_account: NotRequired["aws_sdk_kms.types.principal_id_type.PrincipalIdType"]
    """<p>The Amazon Web Services account under which the grant was issued.</p>"""
    operations: NotRequired["aws_sdk_kms.types.grant_operation_list.GrantOperationList"]
    """<p>The list of operations permitted by the grant.</p>"""
    constraints: NotRequired["aws_sdk_kms.types.grant_constraints.GrantConstraints"]
    """<p>The constraints on the grant, such as encryption context pairs or a SourceArn, that restrict the subsequent operations the grant allows.</p>"""
    grantee_service_principal: NotRequired[
        "aws_sdk_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The Amazon Web Services <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">service principal</a> that gets the permissions in the grant.</p>"""
    retiring_service_principal: NotRequired[
        "aws_sdk_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The Amazon Web Services <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">service principal</a> that can retire the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantListEntry) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "grant_id" in value:
        out["GrantId"] = value["grant_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "creation_date" in value:
        import aws_sdk_kms.types.date_type

        out["CreationDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "grantee_principal" in value:
        out["GranteePrincipal"] = value["grantee_principal"]
    if "retiring_principal" in value:
        out["RetiringPrincipal"] = value["retiring_principal"]
    if "issuing_account" in value:
        out["IssuingAccount"] = value["issuing_account"]
    if "operations" in value:
        import aws_sdk_kms.types.grant_operation_list

        out["Operations"] = (
            aws_sdk_kms.types.grant_operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    if "constraints" in value:
        import aws_sdk_kms.types.grant_constraints

        out["Constraints"] = aws_sdk_kms.types.grant_constraints.serialize_aws_json_1_1(
            value["constraints"]
        )
    if "grantee_service_principal" in value:
        out["GranteeServicePrincipal"] = value["grantee_service_principal"]
    if "retiring_service_principal" in value:
        out["RetiringServicePrincipal"] = value["retiring_service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GrantListEntry:
    out: GrantListEntry = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "GrantId" in data:
        out["grant_id"] = data["GrantId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreationDate" in data:
        import aws_sdk_kms.types.date_type

        out["creation_date"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    if "GranteePrincipal" in data:
        out["grantee_principal"] = data["GranteePrincipal"]
    if "RetiringPrincipal" in data:
        out["retiring_principal"] = data["RetiringPrincipal"]
    if "IssuingAccount" in data:
        out["issuing_account"] = data["IssuingAccount"]
    if "Operations" in data:
        import aws_sdk_kms.types.grant_operation_list

        out["operations"] = (
            aws_sdk_kms.types.grant_operation_list.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    if "Constraints" in data:
        import aws_sdk_kms.types.grant_constraints

        out["constraints"] = (
            aws_sdk_kms.types.grant_constraints.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    if "GranteeServicePrincipal" in data:
        out["grantee_service_principal"] = data["GranteeServicePrincipal"]
    if "RetiringServicePrincipal" in data:
        out["retiring_service_principal"] = data["RetiringServicePrincipal"]
    return out
