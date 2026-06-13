"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.db_password
    import aws_sdk_redshift_serverless.types.db_user
    import aws_sdk_redshift_serverless.types.iam_role_arn_list
    import aws_sdk_redshift_serverless.types.kms_key_id
    import aws_sdk_redshift_serverless.types.log_export_list
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.redshift_idc_application_arn
    import aws_sdk_redshift_serverless.types.tag_list


class CreateNamespaceRequest(TypedDict):
    namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace.</p>"""
    admin_username: NotRequired["aws_sdk_redshift_serverless.types.db_user.DbUser"]
    """<p>The username of the administrator for the first database created in the namespace.</p>"""
    admin_user_password: NotRequired[
        "aws_sdk_redshift_serverless.types.db_password.DbPassword"
    ]
    """<p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>"""
    db_name: NotRequired["str"]
    """<p>The name of the first database created in the namespace.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>"""
    default_iam_role_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>"""
    iam_roles: NotRequired[
        "aws_sdk_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
    ]
    """<p>A list of IAM roles to associate with the namespace.</p>"""
    log_exports: NotRequired[
        "aws_sdk_redshift_serverless.types.log_export_list.LogExportList"
    ]
    """<p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>"""
    tags: NotRequired["aws_sdk_redshift_serverless.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""
    manage_admin_password: NotRequired["bool"]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>"""
    redshift_idc_application_arn: NotRequired[
        "aws_sdk_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
    ]
    """<p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamespaceRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
    if "admin_user_password" in value:
        out["adminUserPassword"] = value["admin_user_password"]
    if "db_name" in value:
        out["dbName"] = value["db_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "default_iam_role_arn" in value:
        out["defaultIamRoleArn"] = value["default_iam_role_arn"]
    if "iam_roles" in value:
        import aws_sdk_redshift_serverless.types.iam_role_arn_list

        out["iamRoles"] = (
            aws_sdk_redshift_serverless.types.iam_role_arn_list.serialize_aws_json_1_1(
                value["iam_roles"]
            )
        )
    if "log_exports" in value:
        import aws_sdk_redshift_serverless.types.log_export_list

        out["logExports"] = (
            aws_sdk_redshift_serverless.types.log_export_list.serialize_aws_json_1_1(
                value["log_exports"]
            )
        )
    if "tags" in value:
        import aws_sdk_redshift_serverless.types.tag_list

        out["tags"] = aws_sdk_redshift_serverless.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "manage_admin_password" in value:
        out["manageAdminPassword"] = value["manage_admin_password"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    if "redshift_idc_application_arn" in value:
        out["redshiftIdcApplicationArn"] = value["redshift_idc_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamespaceRequest:
    out: CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError("CreateNamespaceRequest.namespace_name required")
    if "adminUsername" in data:
        out["admin_username"] = data["adminUsername"]
    if "adminUserPassword" in data:
        out["admin_user_password"] = data["adminUserPassword"]
    if "dbName" in data:
        out["db_name"] = data["dbName"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "defaultIamRoleArn" in data:
        out["default_iam_role_arn"] = data["defaultIamRoleArn"]
    if "iamRoles" in data:
        import aws_sdk_redshift_serverless.types.iam_role_arn_list

        out["iam_roles"] = (
            aws_sdk_redshift_serverless.types.iam_role_arn_list.deserialize_aws_json_1_1(
                data["iamRoles"]
            )
        )
    if "logExports" in data:
        import aws_sdk_redshift_serverless.types.log_export_list

        out["log_exports"] = (
            aws_sdk_redshift_serverless.types.log_export_list.deserialize_aws_json_1_1(
                data["logExports"]
            )
        )
    if "tags" in data:
        import aws_sdk_redshift_serverless.types.tag_list

        out["tags"] = (
            aws_sdk_redshift_serverless.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    if "manageAdminPassword" in data:
        out["manage_admin_password"] = data["manageAdminPassword"]
    if "adminPasswordSecretKmsKeyId" in data:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    if "redshiftIdcApplicationArn" in data:
        out["redshift_idc_application_arn"] = data["redshiftIdcApplicationArn"]
    return out
