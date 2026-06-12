"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.description
    import aws_sdk_directory_service.types.directory_name
    import aws_sdk_directory_service.types.directory_short_name
    import aws_sdk_directory_service.types.directory_size
    import aws_sdk_directory_service.types.directory_vpc_settings
    import aws_sdk_directory_service.types.network_type
    import aws_sdk_directory_service.types.password
    import aws_sdk_directory_service.types.tags


class CreateDirectoryRequest(TypedDict):
    name: "aws_sdk_directory_service.types.directory_name.DirectoryName"
    """<p>The fully qualified name for the directory, such as <code>corp.example.com</code>.</p>"""
    short_name: NotRequired[
        "aws_sdk_directory_service.types.directory_short_name.DirectoryShortName"
    ]
    """<p>The NetBIOS name of the directory, such as <code>CORP</code>.</p>"""
    password: "aws_sdk_directory_service.types.password.Password"
    """<p>The password for the directory administrator. The directory creation process creates a directory administrator account with the user name <code>Administrator</code> and this password.</p> <p>If you need to change the password for the administrator account, you can use the <a>ResetUserPassword</a> API call.</p> <p>The regex pattern for this string is made up of the following conditions:</p> <ul> <li> <p>Length (?=^.{8,64}$) – Must be between 8 and 64 characters</p> </li> </ul> <p>AND any 3 of the following password complexity rules required by Active Directory:</p> <ul> <li> <p>Numbers and upper case and lowercase (?=.*\d)(?=.*[A-Z])(?=.*[a-z])</p> </li> <li> <p>Numbers and special characters and lower case (?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])</p> </li> <li> <p>Special characters and upper case and lower case (?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])</p> </li> <li> <p>Numbers and upper case and special characters (?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s])</p> </li> </ul> <p>For additional information about how Active Directory passwords are enforced, see <a href=\"https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements\">Password must meet complexity requirements</a> on the Microsoft website.</p>"""
    description: NotRequired["aws_sdk_directory_service.types.description.Description"]
    """<p>A description for the directory.</p>"""
    size: "aws_sdk_directory_service.types.directory_size.DirectorySize"
    """<p>The size of the directory.</p>"""
    vpc_settings: NotRequired[
        "aws_sdk_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    ]
    """<p>A <a>DirectoryVpcSettings</a> object that contains additional information for the operation.</p>"""
    tags: NotRequired["aws_sdk_directory_service.types.tags.Tags"]
    """<p>The tags to be assigned to the Simple AD directory.</p>"""
    network_type: NotRequired[
        "aws_sdk_directory_service.types.network_type.NetworkType"
    ]
    """<p>The network type for your directory. Simple AD supports IPv4 and Dual-stack only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    out["Password"] = value["password"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_directory_service.types.directory_size

    out["Size"] = aws_sdk_directory_service.types.directory_size.serialize_aws_json_1_1(
        value["size"]
    )
    if "vpc_settings" in value:
        import aws_sdk_directory_service.types.directory_vpc_settings

        out["VpcSettings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
                value["vpc_settings"]
            )
        )
    if "tags" in value:
        import aws_sdk_directory_service.types.tags

        out["Tags"] = aws_sdk_directory_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "network_type" in value:
        import aws_sdk_directory_service.types.network_type

        out["NetworkType"] = (
            aws_sdk_directory_service.types.network_type.serialize_aws_json_1_1(
                value["network_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDirectoryRequest:
    out: CreateDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDirectoryRequest.name required")
    if "ShortName" in data:
        out["short_name"] = data["ShortName"]
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateDirectoryRequest.password required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Size" in data:
        import aws_sdk_directory_service.types.directory_size

        out["size"] = (
            aws_sdk_directory_service.types.directory_size.deserialize_aws_json_1_1(
                data["Size"]
            )
        )
    else:
        raise DeserializationError("CreateDirectoryRequest.size required")
    if "VpcSettings" in data:
        import aws_sdk_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    if "Tags" in data:
        import aws_sdk_directory_service.types.tags

        out["tags"] = aws_sdk_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NetworkType" in data:
        import aws_sdk_directory_service.types.network_type

        out["network_type"] = (
            aws_sdk_directory_service.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    return out
