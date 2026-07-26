"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.db_password
    import capo_redshift_serverless.types.db_user
    import capo_redshift_serverless.types.iam_role_arn_list
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.log_export_list
    import capo_redshift_serverless.types.namespace_name


class UpdateNamespaceRequest(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>"""
    admin_user_password: NotRequired[
        "capo_redshift_serverless.types.db_password.DbPassword"
    ]
    """<p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>"""
    admin_username: NotRequired["capo_redshift_serverless.types.db_user.DbUser"]
    """<p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>"""
    default_iam_role_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>"""
    iam_roles: NotRequired[
        "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
    ]
    """<p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>"""
    log_exports: NotRequired[
        "capo_redshift_serverless.types.log_export_list.LogExportList"
    ]
    """<p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>"""
    manage_admin_password: NotRequired["bool"]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNamespaceRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "admin_user_password" in value:
        out["adminUserPassword"] = value["admin_user_password"]
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "default_iam_role_arn" in value:
        out["defaultIamRoleArn"] = value["default_iam_role_arn"]
    if "iam_roles" in value:
        import capo_redshift_serverless.types.iam_role_arn_list

        out["iamRoles"] = (
            capo_redshift_serverless.types.iam_role_arn_list.serialize_aws_json_1_1(
                value["iam_roles"]
            )
        )
    if "log_exports" in value:
        import capo_redshift_serverless.types.log_export_list

        out["logExports"] = (
            capo_redshift_serverless.types.log_export_list.serialize_aws_json_1_1(
                value["log_exports"]
            )
        )
    if "manage_admin_password" in value:
        out["manageAdminPassword"] = value["manage_admin_password"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNamespaceRequest:
    out: UpdateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError("UpdateNamespaceRequest.namespace_name required")
    if "adminUserPassword" in data:
        out["admin_user_password"] = data["adminUserPassword"]
    if "adminUsername" in data:
        out["admin_username"] = data["adminUsername"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "defaultIamRoleArn" in data:
        out["default_iam_role_arn"] = data["defaultIamRoleArn"]
    if "iamRoles" in data:
        import capo_redshift_serverless.types.iam_role_arn_list

        out["iam_roles"] = (
            capo_redshift_serverless.types.iam_role_arn_list.deserialize_aws_json_1_1(
                data["iamRoles"]
            )
        )
    if "logExports" in data:
        import capo_redshift_serverless.types.log_export_list

        out["log_exports"] = (
            capo_redshift_serverless.types.log_export_list.deserialize_aws_json_1_1(
                data["logExports"]
            )
        )
    if "manageAdminPassword" in data:
        out["manage_admin_password"] = data["manageAdminPassword"]
    if "adminPasswordSecretKmsKeyId" in data:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    return out
