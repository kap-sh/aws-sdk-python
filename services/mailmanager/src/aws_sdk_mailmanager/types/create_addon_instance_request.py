"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddonInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_subscription_id
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.tag_list


class CreateAddonInstanceRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    addon_subscription_id: (
        "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    )
    """<p>The unique ID of a previously created subscription that an Add On instance is created for. You can only have one instance per subscription.</p>"""
    tags: NotRequired["aws_sdk_mailmanager.types.tag_list.TagList"]
    r"""<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddonInstanceRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AddonSubscriptionId"] = value["addon_subscription_id"]
    if "tags" in value:
        import aws_sdk_mailmanager.types.tag_list

        out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddonInstanceRequest:
    out: CreateAddonInstanceRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "AddonSubscriptionId" in data:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    else:
        raise DeserializationError(
            "CreateAddonInstanceRequest.addon_subscription_id required"
        )
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
