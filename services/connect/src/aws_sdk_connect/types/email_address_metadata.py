"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.alias_configuration_list
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.email_address
    import aws_sdk_connect.types.email_address_arn
    import aws_sdk_connect.types.email_address_display_name
    import aws_sdk_connect.types.email_address_id


class EmailAddressMetadata(TypedDict):
    email_address_id: NotRequired[
        "aws_sdk_connect.types.email_address_id.EmailAddressId"
    ]
    """<p>The identifier of the email address.</p>"""
    email_address_arn: NotRequired[
        "aws_sdk_connect.types.email_address_arn.EmailAddressArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the email address.</p>"""
    email_address: NotRequired["aws_sdk_connect.types.email_address.EmailAddress"]
    """<p>The email address, including the domain.</p>"""
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>The description of the email address.</p>"""
    display_name: NotRequired[
        "aws_sdk_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address.</p>"""
    alias_configurations: NotRequired[
        "aws_sdk_connect.types.alias_configuration_list.AliasConfigurationList"
    ]
    """<p>A list of alias configurations for this email address, showing which email addresses forward to this primary address. Each configuration contains the email address ID of an alias that forwards emails to this address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressMetadata) -> dict:
    out: dict = {}
    if "email_address_id" in value:
        out["EmailAddressId"] = value["email_address_id"]
    if "email_address_arn" in value:
        out["EmailAddressArn"] = value["email_address_arn"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "alias_configurations" in value:
        import aws_sdk_connect.types.alias_configuration_list

        out["AliasConfigurations"] = (
            aws_sdk_connect.types.alias_configuration_list.serialize_json(
                value["alias_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailAddressMetadata:
    out: EmailAddressMetadata = {}  # type: ignore[typeddict-item]
    if "EmailAddressId" in data:
        out["email_address_id"] = data["EmailAddressId"]
    if "EmailAddressArn" in data:
        out["email_address_arn"] = data["EmailAddressArn"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "AliasConfigurations" in data:
        import aws_sdk_connect.types.alias_configuration_list

        out["alias_configurations"] = (
            aws_sdk_connect.types.alias_configuration_list.deserialize_json(
                data["AliasConfigurations"]
            )
        )
    return out
