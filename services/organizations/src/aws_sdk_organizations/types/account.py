"""Generated from Smithy shape ``com.amazonaws.organizations#Account``."""

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
    import aws_sdk_organizations.types.paths
    import aws_sdk_organizations.types.timestamp


class Account(TypedDict):
    id: NotRequired["aws_sdk_organizations.types.account_id.AccountId"]
    """<p>The unique identifier (ID) of the account.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""
    arn: NotRequired["aws_sdk_organizations.types.account_arn.AccountArn"]
    """<p>The Amazon Resource Name (ARN) of the account.</p> <p>For more information about ARNs in Organizations, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies\">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    email: NotRequired["aws_sdk_organizations.types.email.Email"]
    """<p>The email address associated with the Amazon Web Services account.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for this parameter is a string of characters that represents a standard internet email address.</p>"""
    name: NotRequired["aws_sdk_organizations.types.account_name.AccountName"]
    """<p>The friendly name of the account.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    status: NotRequired["aws_sdk_organizations.types.account_status.AccountStatus"]
    """<p>The status of the account in the organization.</p> <important> <p>The <code>Status</code> parameter in the <code>Account</code> object will be retired on September 9, 2026. Although both the account <code>State</code> and account <code>Status</code> parameters are currently available in the Organizations APIs (<code>DescribeAccount</code>, <code>ListAccounts</code>, <code>ListAccountsForParent</code>), we recommend that you update your scripts or other code to use the <code>State</code> parameter instead of <code>Status</code> before September 9, 2026.</p> </important>"""
    state: NotRequired["aws_sdk_organizations.types.account_state.AccountState"]
    """<p>Each state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.</p> <p>For more information about account states and their implications, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_account_state.html\">Monitor the state of your Amazon Web Services accounts </a> in the <i>Organizations User Guide</i>.</p>"""
    paths: NotRequired["aws_sdk_organizations.types.paths.Paths"]
    """<p>The paths in the organization where the account exists.</p>"""
    joined_method: NotRequired[
        "aws_sdk_organizations.types.account_joined_method.AccountJoinedMethod"
    ]
    """<p>The method by which the account joined the organization.</p>"""
    joined_timestamp: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>The date the account became a part of the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Account) -> dict:
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
    if "paths" in value:
        import aws_sdk_organizations.types.paths

        out["Paths"] = aws_sdk_organizations.types.paths.serialize_aws_json_1_1(
            value["paths"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
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
    if "Paths" in data:
        import aws_sdk_organizations.types.paths

        out["paths"] = aws_sdk_organizations.types.paths.deserialize_aws_json_1_1(
            data["Paths"]
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
    return out
