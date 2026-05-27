"""Generated from Smithy shape ``com.amazonaws.eks#UpdateEksAnywhereSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.boolean
    import aws_sdk_eks.types.string


class UpdateEksAnywhereSubscriptionRequest(TypedDict):
    id: "aws_sdk_eks.types.string.String"
    """<p>The ID of the subscription.</p>"""
    auto_renew: "aws_sdk_eks.types.boolean.Boolean"
    """<p>A boolean indicating whether or not to automatically renew the subscription.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEksAnywhereSubscriptionRequest) -> dict:
    out: dict = {}
    out["autoRenew"] = value.get("auto_renew", False)
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateEksAnywhereSubscriptionRequest:
    out: UpdateEksAnywhereSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "autoRenew" in data:
        out["auto_renew"] = data["autoRenew"]
    else:
        out["auto_renew"] = False
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
