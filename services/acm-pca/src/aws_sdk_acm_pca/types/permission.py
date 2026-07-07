"""Generated from Smithy shape ``com.amazonaws.acmpca#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.account_id
    import aws_sdk_acm_pca.types.action_list
    import aws_sdk_acm_pca.types.arn
    import aws_sdk_acm_pca.types.aws_policy
    import aws_sdk_acm_pca.types.principal
    import aws_sdk_acm_pca.types.t_stamp


class Permission(TypedDict, closed=True):
    certificate_authority_arn: NotRequired["aws_sdk_acm_pca.types.arn.Arn"]
    """<p>The Amazon Resource Number (ARN) of the private CA from which the permission was issued.</p>"""
    created_at: NotRequired["aws_sdk_acm_pca.types.t_stamp.TStamp"]
    """<p>The time at which the permission was created.</p>"""
    principal: NotRequired["aws_sdk_acm_pca.types.principal.Principal"]
    """<p>The Amazon Web Services service or entity that holds the permission. At this time, the only valid principal is <code>acm.amazonaws.com</code>.</p>"""
    source_account: NotRequired["aws_sdk_acm_pca.types.account_id.AccountId"]
    """<p>The ID of the account that assigned the permission.</p>"""
    actions: NotRequired["aws_sdk_acm_pca.types.action_list.ActionList"]
    """<p>The private CA actions that can be performed by the designated Amazon Web Services service.</p>"""
    policy: NotRequired["aws_sdk_acm_pca.types.aws_policy.AWSPolicy"]
    """<p>The name of the policy that is associated with the permission.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permission) -> dict:
    out: dict = {}
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "created_at" in value:
        import aws_sdk_acm_pca.types.t_stamp

        out["CreatedAt"] = aws_sdk_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "principal" in value:
        out["Principal"] = value["principal"]
    if "source_account" in value:
        out["SourceAccount"] = value["source_account"]
    if "actions" in value:
        import aws_sdk_acm_pca.types.action_list

        out["Actions"] = aws_sdk_acm_pca.types.action_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if "CreatedAt" in data:
        import aws_sdk_acm_pca.types.t_stamp

        out["created_at"] = aws_sdk_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "Principal" in data:
        out["principal"] = data["Principal"]
    if "SourceAccount" in data:
        out["source_account"] = data["SourceAccount"]
    if "Actions" in data:
        import aws_sdk_acm_pca.types.action_list

        out["actions"] = aws_sdk_acm_pca.types.action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
