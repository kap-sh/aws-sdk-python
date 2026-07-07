"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_environment_id


class DeleteKxClusterRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName"
    """<p>The name of the cluster that you want to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxClusterRequest:
    out: DeleteKxClusterRequest = {}  # type: ignore[typeddict-item]
    return out
