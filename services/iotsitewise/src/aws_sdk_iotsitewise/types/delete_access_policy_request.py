"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.id


class DeleteAccessPolicyRequest(TypedDict, closed=True):
    access_policy_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the access policy to be deleted.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessPolicyRequest:
    out: DeleteAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
