"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteProvisioningProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.provisioning_profile_id


class DeleteProvisioningProfileRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId"
    """<p>The id of the provisioning profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProvisioningProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProvisioningProfileRequest:
    out: DeleteProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
    return out
