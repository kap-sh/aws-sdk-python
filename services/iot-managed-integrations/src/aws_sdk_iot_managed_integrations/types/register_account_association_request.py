"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RegisterAccountAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.device_discovery_id
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class RegisterAccountAssociationRequest(TypedDict):
    managed_thing_id: (
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The identifier of the managed thing to register with the account association.</p>"""
    account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The identifier of the account association to register with the managed thing.</p>"""
    device_discovery_id: (
        "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    )
    """<p>The identifier of the device discovery job associated with this registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAccountAssociationRequest) -> dict:
    out: dict = {}
    out["ManagedThingId"] = value["managed_thing_id"]
    out["AccountAssociationId"] = value["account_association_id"]
    out["DeviceDiscoveryId"] = value["device_discovery_id"]
    return out


def deserialize_json(data: dict) -> RegisterAccountAssociationRequest:
    out: RegisterAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    else:
        raise DeserializationError(
            "RegisterAccountAssociationRequest.managed_thing_id required"
        )
    if "AccountAssociationId" in data:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        raise DeserializationError(
            "RegisterAccountAssociationRequest.account_association_id required"
        )
    if "DeviceDiscoveryId" in data:
        out["device_discovery_id"] = data["DeviceDiscoveryId"]
    else:
        raise DeserializationError(
            "RegisterAccountAssociationRequest.device_discovery_id required"
        )
    return out
