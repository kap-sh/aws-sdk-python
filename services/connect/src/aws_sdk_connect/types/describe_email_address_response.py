"""Generated from Smithy shape ``com.amazonaws.connect#DescribeEmailAddressResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.alias_configuration_list
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.email_address
    import aws_sdk_connect.types.email_address_arn
    import aws_sdk_connect.types.email_address_display_name
    import aws_sdk_connect.types.email_address_id
    import aws_sdk_connect.types.iso8601_datetime
    import aws_sdk_connect.types.tag_map


class DescribeEmailAddressResponse(TypedDict):
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
    display_name: NotRequired[
        "aws_sdk_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address</p>"""
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>The description of the email address.</p>"""
    create_timestamp: NotRequired[
        "aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The email address creation timestamp in ISO 8601 Datetime.</p>"""
    modified_timestamp: NotRequired[
        "aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The email address last modification timestamp in ISO 8601 Datetime.</p>"""
    alias_configurations: NotRequired[
        "aws_sdk_connect.types.alias_configuration_list.AliasConfigurationList"
    ]
    """<p>A list of alias configurations associated with this email address. Contains details about email addresses that forward to this primary email address. The list can contain at most one alias configuration per email address.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEmailAddressResponse) -> dict:
    out: dict = {}
    if "email_address_id" in value:
        out["EmailAddressId"] = value["email_address_id"]
    if "email_address_arn" in value:
        out["EmailAddressArn"] = value["email_address_arn"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "create_timestamp" in value:
        out["CreateTimestamp"] = value["create_timestamp"]
    if "modified_timestamp" in value:
        out["ModifiedTimestamp"] = value["modified_timestamp"]
    if "alias_configurations" in value:
        import aws_sdk_connect.types.alias_configuration_list

        out["AliasConfigurations"] = (
            aws_sdk_connect.types.alias_configuration_list.serialize_json(
                value["alias_configurations"]
            )
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeEmailAddressResponse:
    out: DescribeEmailAddressResponse = {}  # type: ignore[typeddict-item]
    if "EmailAddressId" in data:
        out["email_address_id"] = data["EmailAddressId"]
    if "EmailAddressArn" in data:
        out["email_address_arn"] = data["EmailAddressArn"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreateTimestamp" in data:
        out["create_timestamp"] = data["CreateTimestamp"]
    if "ModifiedTimestamp" in data:
        out["modified_timestamp"] = data["ModifiedTimestamp"]
    if "AliasConfigurations" in data:
        import aws_sdk_connect.types.alias_configuration_list

        out["alias_configurations"] = (
            aws_sdk_connect.types.alias_configuration_list.deserialize_json(
                data["AliasConfigurations"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
