"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.account_id
    import aws_sdk_partnercentral_channel.types.arn
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.date_time
    import aws_sdk_partnercentral_channel.types.program
    import aws_sdk_partnercentral_channel.types.program_management_account_display_name
    import aws_sdk_partnercentral_channel.types.program_management_account_id
    import aws_sdk_partnercentral_channel.types.program_management_account_status
    import aws_sdk_partnercentral_channel.types.revision


class ProgramManagementAccountSummary(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_id.ProgramManagementAccountId"
    ]
    """<p>The unique identifier of the program management account.</p>"""
    revision: NotRequired["aws_sdk_partnercentral_channel.types.revision.Revision"]
    """<p>The current revision number of the program management account.</p>"""
    catalog: NotRequired["aws_sdk_partnercentral_channel.types.catalog.Catalog"]
    """<p>The catalog identifier associated with the account.</p>"""
    program: NotRequired["aws_sdk_partnercentral_channel.types.program.Program"]
    """<p>The program type for the management account.</p>"""
    display_name: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
    ]
    """<p>The display name of the program management account.</p>"""
    account_id: NotRequired["aws_sdk_partnercentral_channel.types.account_id.AccountId"]
    """<p>The AWS account ID associated with the program management account.</p>"""
    arn: NotRequired["aws_sdk_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the program management account.</p>"""
    created_at: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the account was created.</p>"""
    updated_at: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the account was last updated.</p>"""
    start_date: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The start date of the program management account.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_status.ProgramManagementAccountStatus"
    ]
    """<p>The current status of the program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "program" in value:
        import aws_sdk_partnercentral_channel.types.program

        out["program"] = (
            aws_sdk_partnercentral_channel.types.program.serialize_aws_json_1_0(
                value["program"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["createdAt"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["updatedAt"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "start_date" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["startDate"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["start_date"]
            )
        )
    if "status" in value:
        import aws_sdk_partnercentral_channel.types.program_management_account_status

        out["status"] = (
            aws_sdk_partnercentral_channel.types.program_management_account_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgramManagementAccountSummary:
    out: ProgramManagementAccountSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    if "program" in data:
        import aws_sdk_partnercentral_channel.types.program

        out["program"] = (
            aws_sdk_partnercentral_channel.types.program.deserialize_aws_json_1_0(
                data["program"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["created_at"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["updated_at"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "startDate" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["start_date"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    if "status" in data:
        import aws_sdk_partnercentral_channel.types.program_management_account_status

        out["status"] = (
            aws_sdk_partnercentral_channel.types.program_management_account_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
