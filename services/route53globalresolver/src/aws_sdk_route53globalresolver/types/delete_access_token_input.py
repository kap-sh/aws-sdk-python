"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteAccessTokenInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class DeleteAccessTokenInput(TypedDict):
    access_token_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the access token to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessTokenInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessTokenInput:
    out: DeleteAccessTokenInput = {}  # type: ignore[typeddict-item]
    return out
