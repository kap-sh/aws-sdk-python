"""Generated from Smithy shape ``com.amazonaws.kms#ListGrantsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_id_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.limit_type
    import aws_sdk_kms.types.marker_type
    import aws_sdk_kms.types.principal_id_type
    import aws_sdk_kms.types.service_principal_type


class ListGrantsRequest(TypedDict):
    limit: NotRequired["aws_sdk_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>"""
    marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Returns only grants for the specified KMS key. This parameter is required.</p> <p>Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    grant_id: NotRequired["aws_sdk_kms.types.grant_id_type.GrantIdType"]
    """<p>Returns only the grant with the specified grant ID. The grant ID uniquely identifies the grant. </p>"""
    grantee_principal: NotRequired[
        "aws_sdk_kms.types.principal_id_type.PrincipalIdType"
    ]
    """<p>Returns only grants where the specified principal is the grantee principal for the grant.</p> <p>You can specify either <code>GranteePrincipal</code> or <code>GranteeServicePrincipal</code>, but not both.</p>"""
    grantee_service_principal: NotRequired[
        "aws_sdk_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>Returns only grants where the specified Amazon Web Services service principal is the grantee service principal for the grant. This filter is only usable by callers in a service principal.</p> <p>You can specify either <code>GranteePrincipal</code> or <code>GranteeServicePrincipal</code>, but not both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGrantsRequest) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    out["KeyId"] = value["key_id"]
    if "grant_id" in value:
        out["GrantId"] = value["grant_id"]
    if "grantee_principal" in value:
        out["GranteePrincipal"] = value["grantee_principal"]
    if "grantee_service_principal" in value:
        out["GranteeServicePrincipal"] = value["grantee_service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGrantsRequest:
    out: ListGrantsRequest = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("ListGrantsRequest.key_id required")
    if "GrantId" in data:
        out["grant_id"] = data["GrantId"]
    if "GranteePrincipal" in data:
        out["grantee_principal"] = data["GranteePrincipal"]
    if "GranteeServicePrincipal" in data:
        out["grantee_service_principal"] = data["GranteeServicePrincipal"]
    return out
