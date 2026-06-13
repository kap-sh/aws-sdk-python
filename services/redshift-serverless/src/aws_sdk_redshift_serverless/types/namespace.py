"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Namespace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.db_user
    import aws_sdk_redshift_serverless.types.iam_role_arn_list
    import aws_sdk_redshift_serverless.types.kms_key_id
    import aws_sdk_redshift_serverless.types.log_export_list
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.namespace_status


class Namespace(TypedDict):
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) associated with a namespace.</p>"""
    namespace_id: NotRequired["str"]
    """<p>The unique identifier of a namespace.</p>"""
    namespace_name: NotRequired[
        "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in <a href=\"https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p>"""
    admin_username: NotRequired["aws_sdk_redshift_serverless.types.db_user.DbUser"]
    """<p>The username of the administrator for the first database created in the namespace.</p>"""
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
    """<p>The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.</p>"""
    status: NotRequired[
        "aws_sdk_redshift_serverless.types.namespace_status.NamespaceStatus"
    ]
    """<p>The status of the namespace.</p>"""
    creation_date: NotRequired["datetime.datetime"]
    """<p>The date of when the namespace was created.</p>"""
    admin_password_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.</p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>"""
    lakehouse_registration_status: NotRequired["str"]
    """<p>The status of the lakehouse registration for the namespace. Indicates whether the namespace is successfully registered with Amazon Redshift federated permissions.</p>"""
    catalog_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Glue Data Catalog associated with the namespace enabled with Amazon Redshift federated permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Namespace) -> dict:
    out: dict = {}
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
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
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["creationDate"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "admin_password_secret_arn" in value:
        out["adminPasswordSecretArn"] = value["admin_password_secret_arn"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    if "lakehouse_registration_status" in value:
        out["lakehouseRegistrationStatus"] = value["lakehouse_registration_status"]
    if "catalog_arn" in value:
        out["catalogArn"] = value["catalog_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Namespace:
    out: Namespace = {}  # type: ignore[typeddict-item]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "namespaceId" in data:
        out["namespace_id"] = data["namespaceId"]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "adminUsername" in data:
        out["admin_username"] = data["adminUsername"]
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
    if "status" in data:
        out["status"] = data["status"]
    if "creationDate" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["creation_date"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "adminPasswordSecretArn" in data:
        out["admin_password_secret_arn"] = data["adminPasswordSecretArn"]
    if "adminPasswordSecretKmsKeyId" in data:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    if "lakehouseRegistrationStatus" in data:
        out["lakehouse_registration_status"] = data["lakehouseRegistrationStatus"]
    if "catalogArn" in data:
        out["catalog_arn"] = data["catalogArn"]
    return out
