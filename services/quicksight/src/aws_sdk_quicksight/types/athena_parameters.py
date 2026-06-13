"""Generated from Smithy shape ``com.amazonaws.quicksight#AthenaParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.identity_center_configuration
    import aws_sdk_quicksight.types.role_arn
    import aws_sdk_quicksight.types.work_group


class AthenaParameters(TypedDict):
    work_group: NotRequired["aws_sdk_quicksight.types.work_group.WorkGroup"]
    """<p>The workgroup that Amazon Athena uses.</p>"""
    role_arn: NotRequired["aws_sdk_quicksight.types.role_arn.RoleArn"]
    """<p>Use the <code>RoleArn</code> structure to override an account-wide role for a specific Athena data source. For example, say an account administrator has turned off all Athena access with an account-wide role. The administrator can then use <code>RoleArn</code> to bypass the account-wide role and allow Athena access for the single Athena data source that is specified in the structure, even if the account-wide role forbidding Athena access is still active.</p>"""
    consumer_account_role_arn: NotRequired["aws_sdk_quicksight.types.role_arn.RoleArn"]
    """<p>Use <code>ConsumerAccountRoleArn</code> to perform cross-account Athena access. This is an IAM role ARN in the same AWS account as the Athena resources you want to access. Provide this along with <code>RoleArn</code> to enable role-chaining, where Amazon Quick Sight first assumes the <code>RoleArn</code> and then assumes the <code>ConsumerAccountRoleArn</code> to access Athena resources.</p>"""
    identity_center_configuration: NotRequired[
        "aws_sdk_quicksight.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p>An optional parameter that configures IAM Identity Center authentication to grant Quick Sight access to your workgroup.</p> <p>This parameter can only be specified if your Quick Sight account is configured with IAM Identity Center.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AthenaParameters) -> dict:
    out: dict = {}
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "consumer_account_role_arn" in value:
        out["ConsumerAccountRoleArn"] = value["consumer_account_role_arn"]
    if "identity_center_configuration" in value:
        import aws_sdk_quicksight.types.identity_center_configuration

        out["IdentityCenterConfiguration"] = (
            aws_sdk_quicksight.types.identity_center_configuration.serialize_json(
                value["identity_center_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AthenaParameters:
    out: AthenaParameters = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ConsumerAccountRoleArn" in data:
        out["consumer_account_role_arn"] = data["ConsumerAccountRoleArn"]
    if "IdentityCenterConfiguration" in data:
        import aws_sdk_quicksight.types.identity_center_configuration

        out["identity_center_configuration"] = (
            aws_sdk_quicksight.types.identity_center_configuration.deserialize_json(
                data["IdentityCenterConfiguration"]
            )
        )
    return out
