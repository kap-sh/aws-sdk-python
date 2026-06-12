"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetProvisioningProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_id


class GetProvisioningProfileRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId"
    """<p>The id of a provisioning profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProvisioningProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProvisioningProfileRequest:
    out: GetProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
    return out
