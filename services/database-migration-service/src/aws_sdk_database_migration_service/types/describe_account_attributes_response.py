"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeAccountAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.account_quota_list
    import aws_sdk_database_migration_service.types.string


class DescribeAccountAttributesResponse(TypedDict):
    account_quotas: NotRequired[
        "aws_sdk_database_migration_service.types.account_quota_list.AccountQuotaList"
    ]
    """<p>Account quota information.</p>"""
    unique_account_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>A unique DMS identifier for an account in a particular Amazon Web Services Region. The value of this identifier has the following format: <code>c99999999999</code>. DMS uses this identifier to name artifacts. For example, DMS uses this identifier to name the default Amazon S3 bucket for storing task assessment reports in a given Amazon Web Services Region. The format of this S3 bucket name is the following: <code>dms-<i>AccountNumber</i>-<i>UniqueAccountIdentifier</i>.</code> Here is an example name for this default S3 bucket: <code>dms-111122223333-c44445555666</code>.</p> <note> <p>DMS supports the <code>UniqueAccountIdentifier</code> parameter in versions 3.1.4 and later.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountAttributesResponse) -> dict:
    out: dict = {}
    if "account_quotas" in value:
        import aws_sdk_database_migration_service.types.account_quota_list

        out["AccountQuotas"] = (
            aws_sdk_database_migration_service.types.account_quota_list.serialize_aws_json_1_1(
                value["account_quotas"]
            )
        )
    if "unique_account_identifier" in value:
        out["UniqueAccountIdentifier"] = value["unique_account_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountAttributesResponse:
    out: DescribeAccountAttributesResponse = {}  # type: ignore[typeddict-item]
    if "AccountQuotas" in data:
        import aws_sdk_database_migration_service.types.account_quota_list

        out["account_quotas"] = (
            aws_sdk_database_migration_service.types.account_quota_list.deserialize_aws_json_1_1(
                data["AccountQuotas"]
            )
        )
    if "UniqueAccountIdentifier" in data:
        out["unique_account_identifier"] = data["UniqueAccountIdentifier"]
    return out
