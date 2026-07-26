"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeregisterAccountAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.managed_thing_id


class DeregisterAccountAssociationRequest(TypedDict, closed=True):
    managed_thing_id: (
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The identifier of the managed thing to be deregistered from the account association.</p>"""
    account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The unique identifier of the account association to be deregistered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterAccountAssociationRequest) -> dict:
    out: dict = {}
    out["ManagedThingId"] = value["managed_thing_id"]
    out["AccountAssociationId"] = value["account_association_id"]
    return out


def deserialize_json(data: dict) -> DeregisterAccountAssociationRequest:
    out: DeregisterAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    else:
        raise DeserializationError(
            "DeregisterAccountAssociationRequest.managed_thing_id required"
        )
    if "AccountAssociationId" in data:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        raise DeserializationError(
            "DeregisterAccountAssociationRequest.account_association_id required"
        )
    return out
