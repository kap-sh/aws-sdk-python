"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.lifecycle_policy_arn


class CreateLifecyclePolicyResponse(TypedDict, closed=True):
    client_token: NotRequired["capo_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    lifecycle_policy_arn: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy that the request created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "lifecycle_policy_arn" in value:
        out["lifecyclePolicyArn"] = value["lifecycle_policy_arn"]
    return out


def deserialize_json(data: dict) -> CreateLifecyclePolicyResponse:
    out: CreateLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "lifecyclePolicyArn" in data:
        out["lifecycle_policy_arn"] = data["lifecyclePolicyArn"]
    return out
