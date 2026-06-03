"""Generated from Smithy shape ``com.amazonaws.kms#GrantListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.date_type
    import awd_sdk_kms.types.grant_constraints
    import awd_sdk_kms.types.grant_id_type
    import awd_sdk_kms.types.grant_name_type
    import awd_sdk_kms.types.grant_operation_list
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.principal_id_type
    import awd_sdk_kms.types.service_principal_type


class GrantListEntry(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The unique identifier for the KMS key to which the grant applies.</p>"""
    grant_id: NotRequired["awd_sdk_kms.types.grant_id_type.GrantIdType"]
    """<p>The unique identifier for the grant.</p>"""
    name: NotRequired["awd_sdk_kms.types.grant_name_type.GrantNameType"]
    """<p>The friendly name that identifies the grant. If a name was provided in the <a>CreateGrant</a> request, that name is returned. Otherwise this value is null.</p>"""
    creation_date: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>The date and time when the grant was created.</p>"""
    grantee_principal: NotRequired[
        "awd_sdk_kms.types.principal_id_type.PrincipalIdType"
    ]
    """<p>The identity that gets the permissions in the grant.</p> <p>When a grant is created with the <code>GranteePrincipal</code> field, the <code>ListGrants</code> response usually contains the user or role designated as the grantee principal in the grant. However, if the grantee principal is an Amazon Web Services service, the <code>GranteePrincipal</code> field contains an Amazon Web Services <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">service principal</a>, which might correspond to several different grantee principals, such as an IAM user, IAM role, or Amazon Web Services account.</p>"""
    retiring_principal: NotRequired[
        "awd_sdk_kms.types.principal_id_type.PrincipalIdType"
    ]
    """<p>The principal that can retire the grant.</p>"""
    issuing_account: NotRequired["awd_sdk_kms.types.principal_id_type.PrincipalIdType"]
    """<p>The Amazon Web Services account under which the grant was issued.</p>"""
    operations: NotRequired["awd_sdk_kms.types.grant_operation_list.GrantOperationList"]
    """<p>The list of operations permitted by the grant.</p>"""
    constraints: NotRequired["awd_sdk_kms.types.grant_constraints.GrantConstraints"]
    """<p>The constraints on the grant, such as encryption context pairs or a SourceArn, that restrict the subsequent operations the grant allows.</p>"""
    grantee_service_principal: NotRequired[
        "awd_sdk_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The Amazon Web Services <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">service principal</a> that gets the permissions in the grant.</p>"""
    retiring_service_principal: NotRequired[
        "awd_sdk_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The Amazon Web Services <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">service principal</a> that can retire the grant.</p>"""
