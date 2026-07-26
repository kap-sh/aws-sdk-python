"""Generated from Smithy shape ``com.amazonaws.deadline#FleetMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.deadline_principal_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.membership_level


class FleetMember(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>The principal ID of the fleet member.</p>"""
    principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType"
    """<p>The principal type of the fleet member.</p>"""
    identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId"
    """<p>The identity store ID.</p>"""
    membership_level: "capo_deadline.types.membership_level.MembershipLevel"
    """<p>The fleet member's membership level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetMember) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["principalId"] = value["principal_id"]
    import capo_deadline.types.deadline_principal_type

    out["principalType"] = capo_deadline.types.deadline_principal_type.serialize_json(
        value["principal_type"]
    )
    out["identityStoreId"] = value["identity_store_id"]
    import capo_deadline.types.membership_level

    out["membershipLevel"] = capo_deadline.types.membership_level.serialize_json(
        value["membership_level"]
    )
    return out


def deserialize_json(data: dict) -> FleetMember:
    out: FleetMember = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("FleetMember.farm_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("FleetMember.fleet_id required")
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    else:
        raise DeserializationError("FleetMember.principal_id required")
    if "principalType" in data:
        import capo_deadline.types.deadline_principal_type

        out["principal_type"] = (
            capo_deadline.types.deadline_principal_type.deserialize_json(
                data["principalType"]
            )
        )
    else:
        raise DeserializationError("FleetMember.principal_type required")
    if "identityStoreId" in data:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        raise DeserializationError("FleetMember.identity_store_id required")
    if "membershipLevel" in data:
        import capo_deadline.types.membership_level

        out["membership_level"] = capo_deadline.types.membership_level.deserialize_json(
            data["membershipLevel"]
        )
    else:
        raise DeserializationError("FleetMember.membership_level required")
    return out
