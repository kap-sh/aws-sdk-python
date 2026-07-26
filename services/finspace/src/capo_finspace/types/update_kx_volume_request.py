"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token_string
    import capo_finspace.types.description
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_nas1_configuration
    import capo_finspace.types.kx_volume_name


class UpdateKxVolumeRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment where you created the storage volume. </p>"""
    volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName"
    """<p> A unique identifier for the volume.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p> A description of the volume. </p>"""
    client_token: NotRequired[
        "capo_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    nas1_configuration: NotRequired[
        "capo_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
    ]
    """<p> Specifies the configuration for the Network attached storage (NAS_1) file system volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxVolumeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "nas1_configuration" in value:
        import capo_finspace.types.kx_nas1_configuration

        out["nas1Configuration"] = (
            capo_finspace.types.kx_nas1_configuration.serialize_json(
                value["nas1_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKxVolumeRequest:
    out: UpdateKxVolumeRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "nas1Configuration" in data:
        import capo_finspace.types.kx_nas1_configuration

        out["nas1_configuration"] = (
            capo_finspace.types.kx_nas1_configuration.deserialize_json(
                data["nas1Configuration"]
            )
        )
    return out
