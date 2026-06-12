"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteProvisioningProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_id


class DeleteProvisioningProfileRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId"
    """<p>The id of the provisioning profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProvisioningProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProvisioningProfileRequest:
    out: DeleteProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
    return out
