"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token_string
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_volume_name


class DeleteKxVolumeRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName"
    """<p> The name of the volume that you want to delete. </p>"""
    client_token: NotRequired[
        "capo_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxVolumeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxVolumeRequest:
    out: DeleteKxVolumeRequest = {}  # type: ignore[typeddict-item]
    return out
