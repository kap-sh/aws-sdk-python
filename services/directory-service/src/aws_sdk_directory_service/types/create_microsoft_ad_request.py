"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateMicrosoftADRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.description
    import aws_sdk_directory_service.types.directory_edition
    import aws_sdk_directory_service.types.directory_name
    import aws_sdk_directory_service.types.directory_short_name
    import aws_sdk_directory_service.types.directory_vpc_settings
    import aws_sdk_directory_service.types.network_type
    import aws_sdk_directory_service.types.password
    import aws_sdk_directory_service.types.tags


class CreateMicrosoftADRequest(TypedDict):
    name: "aws_sdk_directory_service.types.directory_name.DirectoryName"
    """<p>The fully qualified domain name for the Managed Microsoft AD directory, such as <code>corp.example.com</code>. This name will resolve inside your VPC only. It does not need to be publicly resolvable.</p>"""
    short_name: NotRequired[
        "aws_sdk_directory_service.types.directory_short_name.DirectoryShortName"
    ]
    """<p>The NetBIOS name for your domain, such as <code>CORP</code>. If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, <code>CORP</code> for the directory DNS <code>corp.example.com</code>. </p>"""
    password: "aws_sdk_directory_service.types.password.Password"
    """<p>The password for the default administrative user named <code>Admin</code>.</p> <p>If you need to change the password for the administrator account, you can use the <a>ResetUserPassword</a> API call.</p>"""
    description: NotRequired["aws_sdk_directory_service.types.description.Description"]
    """<p>A description for the directory. This label will appear on the Amazon Web Services console <code>Directory Details</code> page after the directory is created.</p>"""
    vpc_settings: (
        "aws_sdk_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    )
    """<p>Contains VPC information for the <a>CreateDirectory</a> or <a>CreateMicrosoftAD</a> operation.</p>"""
    edition: NotRequired[
        "aws_sdk_directory_service.types.directory_edition.DirectoryEdition"
    ]
    """<p>Managed Microsoft AD is available in two editions: <code>Standard</code> and <code>Enterprise</code>. <code>Enterprise</code> is the default.</p>"""
    tags: NotRequired["aws_sdk_directory_service.types.tags.Tags"]
    """<p>The tags to be assigned to the Managed Microsoft AD directory.</p>"""
    network_type: NotRequired[
        "aws_sdk_directory_service.types.network_type.NetworkType"
    ]
    """<p> The network type for your domain. The default value is <code>IPv4</code> or <code>IPv6</code> based on the provided subnet capabilities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMicrosoftADRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    out["Password"] = value["password"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_directory_service.types.directory_vpc_settings

    out["VpcSettings"] = (
        aws_sdk_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
            value["vpc_settings"]
        )
    )
    if "edition" in value:
        import aws_sdk_directory_service.types.directory_edition

        out["Edition"] = (
            aws_sdk_directory_service.types.directory_edition.serialize_aws_json_1_1(
                value["edition"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateMicrosoftADRequest:
    out: CreateMicrosoftADRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateMicrosoftADRequest.name required")
    if "ShortName" in data:
        out["short_name"] = data["ShortName"]
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateMicrosoftADRequest.password required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "VpcSettings" in data:
        import aws_sdk_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    else:
        raise DeserializationError("CreateMicrosoftADRequest.vpc_settings required")
    if "Edition" in data:
        import aws_sdk_directory_service.types.directory_edition

        out["edition"] = (
            aws_sdk_directory_service.types.directory_edition.deserialize_aws_json_1_1(
                data["Edition"]
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
