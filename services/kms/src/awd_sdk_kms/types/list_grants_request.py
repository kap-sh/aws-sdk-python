"""Generated from Smithy shape ``com.amazonaws.kms#ListGrantsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.grant_id_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.limit_type
    import awd_sdk_kms.types.marker_type
    import awd_sdk_kms.types.principal_id_type
    import awd_sdk_kms.types.service_principal_type


class ListGrantsRequest(TypedDict):
    limit: NotRequired["awd_sdk_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>"""
    marker: NotRequired["awd_sdk_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""
    key_id: "awd_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Returns only grants for the specified KMS key. This parameter is required.</p> <p>Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    grant_id: NotRequired["awd_sdk_kms.types.grant_id_type.GrantIdType"]
    """<p>Returns only the grant with the specified grant ID. The grant ID uniquely identifies the grant. </p>"""
    grantee_principal: NotRequired[
        "awd_sdk_kms.types.principal_id_type.PrincipalIdType"
    ]
    """<p>Returns only grants where the specified principal is the grantee principal for the grant.</p> <p>You can specify either <code>GranteePrincipal</code> or <code>GranteeServicePrincipal</code>, but not both.</p>"""
    grantee_service_principal: NotRequired[
        "awd_sdk_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>Returns only grants where the specified Amazon Web Services service principal is the grantee service principal for the grant. This filter is only usable by callers in a service principal.</p> <p>You can specify either <code>GranteePrincipal</code> or <code>GranteeServicePrincipal</code>, but not both.</p>"""
