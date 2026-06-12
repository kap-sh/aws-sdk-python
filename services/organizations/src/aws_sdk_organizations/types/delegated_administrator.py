"""Generated from Smithy shape ``com.amazonaws.organizations#DelegatedAdministrator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.account_arn
    import aws_sdk_organizations.types.account_id
    import aws_sdk_organizations.types.account_joined_method
    import aws_sdk_organizations.types.account_name
    import aws_sdk_organizations.types.account_state
    import aws_sdk_organizations.types.account_status
    import aws_sdk_organizations.types.email
    import aws_sdk_organizations.types.timestamp


class DelegatedAdministrator(TypedDict):
    id: NotRequired["aws_sdk_organizations.types.account_id.AccountId"]
    """<p>The unique identifier (ID) of the delegated administrator's account.</p>"""
    arn: NotRequired["aws_sdk_organizations.types.account_arn.AccountArn"]
    """<p>The Amazon Resource Name (ARN) of the delegated administrator's account.</p>"""
    email: NotRequired["aws_sdk_organizations.types.email.Email"]
    """<p>The email address that is associated with the delegated administrator's Amazon Web Services account.</p>"""
    name: NotRequired["aws_sdk_organizations.types.account_name.AccountName"]
    """<p>The friendly name of the delegated administrator's account.</p>"""
    status: NotRequired["aws_sdk_organizations.types.account_status.AccountStatus"]
    """<p>The status of the delegated administrator's account in the organization.</p>"""
    state: NotRequired["aws_sdk_organizations.types.account_state.AccountState"]
    """<p>Each state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.</p> <p>For more information about account states and their implications, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_account_state.html\">Monitor the state of your Amazon Web Services accounts </a> in the <i>Organizations User Guide</i>.</p>"""
    joined_method: NotRequired[
        "aws_sdk_organizations.types.account_joined_method.AccountJoinedMethod"
    ]
    """<p>The method by which the delegated administrator's account joined the organization.</p>"""
    joined_timestamp: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>The date when the delegated administrator's account became a part of the organization.</p>"""
    delegation_enabled_date: NotRequired[
        "aws_sdk_organizations.types.timestamp.Timestamp"
    ]
    """<p>The date when the account was made a delegated administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DelegatedAdministrator) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_organizations.types.account_status

        out["Status"] = (
            aws_sdk_organizations.types.account_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "state" in value:
        import aws_sdk_organizations.types.account_state

        out["State"] = aws_sdk_organizations.types.account_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "joined_method" in value:
        import aws_sdk_organizations.types.account_joined_method

        out["JoinedMethod"] = (
            aws_sdk_organizations.types.account_joined_method.serialize_aws_json_1_1(
                value["joined_method"]
            )
        )
    if "joined_timestamp" in value:
        import aws_sdk_organizations.types.timestamp

        out["JoinedTimestamp"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["joined_timestamp"]
            )
        )
    if "delegation_enabled_date" in value:
        import aws_sdk_organizations.types.timestamp

        out["DelegationEnabledDate"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["delegation_enabled_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DelegatedAdministrator:
    out: DelegatedAdministrator = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_organizations.types.account_status

        out["status"] = (
            aws_sdk_organizations.types.account_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "State" in data:
        import aws_sdk_organizations.types.account_state

        out["state"] = (
            aws_sdk_organizations.types.account_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "JoinedMethod" in data:
        import aws_sdk_organizations.types.account_joined_method

        out["joined_method"] = (
            aws_sdk_organizations.types.account_joined_method.deserialize_aws_json_1_1(
                data["JoinedMethod"]
            )
        )
    if "JoinedTimestamp" in data:
        import aws_sdk_organizations.types.timestamp

        out["joined_timestamp"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["JoinedTimestamp"]
            )
        )
    if "DelegationEnabledDate" in data:
        import aws_sdk_organizations.types.timestamp

        out["delegation_enabled_date"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["DelegationEnabledDate"]
            )
        )
    return out
