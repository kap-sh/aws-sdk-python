"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetsFromLakeFormationTagPolicyResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.aws_account_id
    import aws_sdk_dataexchange.types.database_lf_tag_policy_and_permissions
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.role_arn
    import aws_sdk_dataexchange.types.table_lf_tag_policy_and_permissions


class ImportAssetsFromLakeFormationTagPolicyResponseDetails(TypedDict, closed=True):
    catalog_id: "aws_sdk_dataexchange.types.aws_account_id.AwsAccountId"
    """<p>The identifier for the AWS Glue Data Catalog.</p>"""
    database: NotRequired[
        "aws_sdk_dataexchange.types.database_lf_tag_policy_and_permissions.DatabaseLFTagPolicyAndPermissions"
    ]
    """<p>A structure for the database object.</p>"""
    table: NotRequired[
        "aws_sdk_dataexchange.types.table_lf_tag_policy_and_permissions.TableLFTagPolicyAndPermissions"
    ]
    """<p>A structure for the table object.</p>"""
    role_arn: "aws_sdk_dataexchange.types.role_arn.RoleArn"
    """<p>The IAM role's ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions to AWS Lake Formation data permissions.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ImportAssetsFromLakeFormationTagPolicyResponseDetails,
) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    if "database" in value:
        import aws_sdk_dataexchange.types.database_lf_tag_policy_and_permissions

        out["Database"] = (
            aws_sdk_dataexchange.types.database_lf_tag_policy_and_permissions.serialize_json(
                value["database"]
            )
        )
    if "table" in value:
        import aws_sdk_dataexchange.types.table_lf_tag_policy_and_permissions

        out["Table"] = (
            aws_sdk_dataexchange.types.table_lf_tag_policy_and_permissions.serialize_json(
                value["table"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(
    data: dict,
) -> ImportAssetsFromLakeFormationTagPolicyResponseDetails:
    out: ImportAssetsFromLakeFormationTagPolicyResponseDetails = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromLakeFormationTagPolicyResponseDetails.catalog_id required"
        )
    if "Database" in data:
        import aws_sdk_dataexchange.types.database_lf_tag_policy_and_permissions

        out["database"] = (
            aws_sdk_dataexchange.types.database_lf_tag_policy_and_permissions.deserialize_json(
                data["Database"]
            )
        )
    if "Table" in data:
        import aws_sdk_dataexchange.types.table_lf_tag_policy_and_permissions

        out["table"] = (
            aws_sdk_dataexchange.types.table_lf_tag_policy_and_permissions.deserialize_json(
                data["Table"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError(
            "ImportAssetsFromLakeFormationTagPolicyResponseDetails.role_arn required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromLakeFormationTagPolicyResponseDetails.data_set_id required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromLakeFormationTagPolicyResponseDetails.revision_id required"
        )
    return out
