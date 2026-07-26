"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.subscription_principal
    import capo_qbusiness.types.subscription_type


class CreateSubscriptionRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application the subscription should be added to.</p>"""
    principal: "capo_qbusiness.types.subscription_principal.SubscriptionPrincipal"
    """<p>The IAM Identity Center <code>UserId</code> or <code>GroupId</code> of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.</p>"""
    type: "capo_qbusiness.types.subscription_type.SubscriptionType"
    """<p>The type of Amazon Q Business subscription you want to create.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create a subscription for your Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionRequest) -> dict:
    out: dict = {}
    import capo_qbusiness.types.subscription_principal

    out["principal"] = capo_qbusiness.types.subscription_principal.serialize_json(
        value["principal"]
    )
    import capo_qbusiness.types.subscription_type

    out["type"] = capo_qbusiness.types.subscription_type.serialize_json(value["type"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSubscriptionRequest:
    out: CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        import capo_qbusiness.types.subscription_principal

        out["principal"] = capo_qbusiness.types.subscription_principal.deserialize_json(
            data["principal"]
        )
    else:
        raise DeserializationError("CreateSubscriptionRequest.principal required")
    if "type" in data:
        import capo_qbusiness.types.subscription_type

        out["type"] = capo_qbusiness.types.subscription_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateSubscriptionRequest.type required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
