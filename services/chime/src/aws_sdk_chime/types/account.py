"""Generated from Smithy shape ``com.amazonaws.chime#Account``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.account_status
    import aws_sdk_chime.types.account_type
    import aws_sdk_chime.types.iso8601_timestamp
    import aws_sdk_chime.types.license
    import aws_sdk_chime.types.license_list
    import aws_sdk_chime.types.signin_delegate_group_list
    import aws_sdk_chime.types.string


class Account(TypedDict, closed=True):
    aws_account_id: "aws_sdk_chime.types.string.String"
    """<p>The AWS account ID.</p>"""
    account_id: "aws_sdk_chime.types.string.String"
    """<p>The Amazon Chime account ID.</p>"""
    name: "aws_sdk_chime.types.string.String"
    """<p>The Amazon Chime account name.</p>"""
    account_type: NotRequired["aws_sdk_chime.types.account_type.AccountType"]
    r"""<p>The Amazon Chime account type. For more information about different account types, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\">Managing Your Amazon Chime Accounts</a> in the <i>Amazon Chime Administration Guide</i>.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The Amazon Chime account creation timestamp, in ISO 8601 format.</p>"""
    default_license: NotRequired["aws_sdk_chime.types.license.License"]
    """<p>The default license for the Amazon Chime account.</p>"""
    supported_licenses: NotRequired["aws_sdk_chime.types.license_list.LicenseList"]
    """<p>Supported licenses for the Amazon Chime account.</p>"""
    account_status: NotRequired["aws_sdk_chime.types.account_status.AccountStatus"]
    """<p>The status of the account.</p>"""
    signin_delegate_groups: NotRequired[
        "aws_sdk_chime.types.signin_delegate_group_list.SigninDelegateGroupList"
    ]
    """<p>The sign-in delegate groups associated with the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    out["AwsAccountId"] = value["aws_account_id"]
    out["AccountId"] = value["account_id"]
    out["Name"] = value["name"]
    if "account_type" in value:
        import aws_sdk_chime.types.account_type

        out["AccountType"] = aws_sdk_chime.types.account_type.serialize_json(
            value["account_type"]
        )
    if "created_timestamp" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["CreatedTimestamp"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "default_license" in value:
        import aws_sdk_chime.types.license

        out["DefaultLicense"] = aws_sdk_chime.types.license.serialize_json(
            value["default_license"]
        )
    if "supported_licenses" in value:
        import aws_sdk_chime.types.license_list

        out["SupportedLicenses"] = aws_sdk_chime.types.license_list.serialize_json(
            value["supported_licenses"]
        )
    if "account_status" in value:
        import aws_sdk_chime.types.account_status

        out["AccountStatus"] = aws_sdk_chime.types.account_status.serialize_json(
            value["account_status"]
        )
    if "signin_delegate_groups" in value:
        import aws_sdk_chime.types.signin_delegate_group_list

        out["SigninDelegateGroups"] = (
            aws_sdk_chime.types.signin_delegate_group_list.serialize_json(
                value["signin_delegate_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        raise DeserializationError("Account.aws_account_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("Account.account_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Account.name required")
    if "AccountType" in data:
        import aws_sdk_chime.types.account_type

        out["account_type"] = aws_sdk_chime.types.account_type.deserialize_json(
            data["AccountType"]
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "DefaultLicense" in data:
        import aws_sdk_chime.types.license

        out["default_license"] = aws_sdk_chime.types.license.deserialize_json(
            data["DefaultLicense"]
        )
    if "SupportedLicenses" in data:
        import aws_sdk_chime.types.license_list

        out["supported_licenses"] = aws_sdk_chime.types.license_list.deserialize_json(
            data["SupportedLicenses"]
        )
    if "AccountStatus" in data:
        import aws_sdk_chime.types.account_status

        out["account_status"] = aws_sdk_chime.types.account_status.deserialize_json(
            data["AccountStatus"]
        )
    if "SigninDelegateGroups" in data:
        import aws_sdk_chime.types.signin_delegate_group_list

        out["signin_delegate_groups"] = (
            aws_sdk_chime.types.signin_delegate_group_list.deserialize_json(
                data["SigninDelegateGroups"]
            )
        )
    return out
