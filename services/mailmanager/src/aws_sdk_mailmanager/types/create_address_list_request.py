"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_list_name
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.tag_list


class CreateAddressListRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    address_list_name: "aws_sdk_mailmanager.types.address_list_name.AddressListName"
    """<p>A user-friendly name for the address list.</p>"""
    tags: NotRequired["aws_sdk_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AddressListName"] = value["address_list_name"]
    if "tags" in value:
        import aws_sdk_mailmanager.types.tag_list

        out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListRequest:
    out: CreateAddressListRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "AddressListName" in data:
        out["address_list_name"] = data["AddressListName"]
    else:
        raise DeserializationError(
            "CreateAddressListRequest.address_list_name required"
        )
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
