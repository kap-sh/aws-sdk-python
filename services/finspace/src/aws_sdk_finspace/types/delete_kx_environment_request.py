"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.id_type


class DeleteKxEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxEnvironmentRequest:
    out: DeleteKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
