"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DescribeUserResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.attributes
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.distinguished_name
    import aws_sdk_directory_service_data.types.email_address
    import aws_sdk_directory_service_data.types.given_name
    import aws_sdk_directory_service_data.types.realm
    import aws_sdk_directory_service_data.types.sid
    import aws_sdk_directory_service_data.types.surname
    import aws_sdk_directory_service_data.types.user_name
    import aws_sdk_directory_service_data.types.user_principal_name


class DescribeUserResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the user. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the user. </p>"""
    sid: NotRequired["aws_sdk_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the user. </p>"""
    sam_account_name: NotRequired[
        "aws_sdk_directory_service_data.types.user_name.UserName"
    ]
    """<p> The name of the user. </p>"""
    distinguished_name: NotRequired[
        "aws_sdk_directory_service_data.types.distinguished_name.DistinguishedName"
    ]
    r"""<p> The <a href=\"https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name\">distinguished name</a> of the object. </p>"""
    user_principal_name: NotRequired[
        "aws_sdk_directory_service_data.types.user_principal_name.UserPrincipalName"
    ]
    r"""<p> The UPN that is an Internet-style login name for a user and is based on the Internet standard <a href=\"https://datatracker.ietf.org/doc/html/rfc822\">RFC 822</a>. The UPN is shorter than the distinguished name and easier to remember. </p>"""
    email_address: NotRequired[
        "aws_sdk_directory_service_data.types.email_address.EmailAddress"
    ]
    """<p> The email address of the user. </p>"""
    given_name: NotRequired["aws_sdk_directory_service_data.types.given_name.GivenName"]
    """<p> The first name of the user. </p>"""
    surname: NotRequired["aws_sdk_directory_service_data.types.surname.Surname"]
    """<p> The last name of the user. </p>"""
    enabled: NotRequired["bool"]
    """<p> Indicates whether the user account is active. </p>"""
    other_attributes: NotRequired[
        "aws_sdk_directory_service_data.types.attributes.Attributes"
    ]
    """<p> The attribute values that are returned for the attribute names that are included in the request. </p> <note> <p> Attribute names are case insensitive. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "sid" in value:
        out["SID"] = value["sid"]
    if "sam_account_name" in value:
        out["SAMAccountName"] = value["sam_account_name"]
    if "distinguished_name" in value:
        out["DistinguishedName"] = value["distinguished_name"]
    if "user_principal_name" in value:
        out["UserPrincipalName"] = value["user_principal_name"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "other_attributes" in value:
        import aws_sdk_directory_service_data.types.attributes

        out["OtherAttributes"] = (
            aws_sdk_directory_service_data.types.attributes.serialize_json(
                value["other_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeUserResult:
    out: DescribeUserResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "SID" in data:
        out["sid"] = data["SID"]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    if "DistinguishedName" in data:
        out["distinguished_name"] = data["DistinguishedName"]
    if "UserPrincipalName" in data:
        out["user_principal_name"] = data["UserPrincipalName"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "OtherAttributes" in data:
        import aws_sdk_directory_service_data.types.attributes

        out["other_attributes"] = (
            aws_sdk_directory_service_data.types.attributes.deserialize_json(
                data["OtherAttributes"]
            )
        )
    return out
