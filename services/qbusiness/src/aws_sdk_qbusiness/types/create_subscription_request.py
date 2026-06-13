"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.subscription_principal
    import aws_sdk_qbusiness.types.subscription_type


class CreateSubscriptionRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application the subscription should be added to.</p>"""
    principal: "aws_sdk_qbusiness.types.subscription_principal.SubscriptionPrincipal"
    """<p>The IAM Identity Center <code>UserId</code> or <code>GroupId</code> of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.</p>"""
    type: "aws_sdk_qbusiness.types.subscription_type.SubscriptionType"
    """<p>The type of Amazon Q Business subscription you want to create.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create a subscription for your Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionRequest) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.subscription_principal

    out["principal"] = aws_sdk_qbusiness.types.subscription_principal.serialize_json(
        value["principal"]
    )
    import aws_sdk_qbusiness.types.subscription_type

    out["type"] = aws_sdk_qbusiness.types.subscription_type.serialize_json(
        value["type"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSubscriptionRequest:
    out: CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        import aws_sdk_qbusiness.types.subscription_principal

        out["principal"] = (
            aws_sdk_qbusiness.types.subscription_principal.deserialize_json(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriptionRequest.principal required")
    if "type" in data:
        import aws_sdk_qbusiness.types.subscription_type

        out["type"] = aws_sdk_qbusiness.types.subscription_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateSubscriptionRequest.type required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
