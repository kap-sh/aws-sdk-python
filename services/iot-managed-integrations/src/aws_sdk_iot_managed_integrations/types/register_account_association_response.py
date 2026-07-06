"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RegisterAccountAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.device_discovery_id
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class RegisterAccountAssociationResponse(TypedDict, closed=True):
    account_association_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    ]
    """<p>The identifier of the account association that was registered.</p>"""
    device_discovery_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    ]
    """<p>The identifier of the device discovery job associated with this registration.</p>"""
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The identifier of the managed thing that was registered with the account association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAccountAssociationResponse) -> dict:
    out: dict = {}
    if "account_association_id" in value:
        out["AccountAssociationId"] = value["account_association_id"]
    if "device_discovery_id" in value:
        out["DeviceDiscoveryId"] = value["device_discovery_id"]
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    return out


def deserialize_json(data: dict) -> RegisterAccountAssociationResponse:
    out: RegisterAccountAssociationResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssociationId" in data:
        out["account_association_id"] = data["AccountAssociationId"]
    if "DeviceDiscoveryId" in data:
        out["device_discovery_id"] = data["DeviceDiscoveryId"]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    return out
