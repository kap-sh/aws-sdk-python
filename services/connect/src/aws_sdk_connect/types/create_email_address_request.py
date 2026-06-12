"""Generated from Smithy shape ``com.amazonaws.connect#CreateEmailAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.email_address
    import aws_sdk_connect.types.email_address_display_name
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map


class CreateEmailAddressRequest(TypedDict):
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>The description of the email address.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    email_address: "aws_sdk_connect.types.email_address.EmailAddress"
    """<p>The email address, including the domain.</p>"""
    display_name: NotRequired[
        "aws_sdk_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailAddressRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["EmailAddress"] = value["email_address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateEmailAddressRequest:
    out: CreateEmailAddressRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("CreateEmailAddressRequest.email_address required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
