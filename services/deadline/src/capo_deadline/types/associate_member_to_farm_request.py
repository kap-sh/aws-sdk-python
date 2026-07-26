"""Generated from Smithy shape ``com.amazonaws.deadline#AssociateMemberToFarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.deadline_principal_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.membership_level
    import capo_deadline.types.region


class AssociateMemberToFarmRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The ID of the farm to associate with the member.</p>"""
    principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType"
    """<p>The principal type of the member to associate with the farm.</p>"""
    identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId"
    """<p>The identity store ID of the member to associate with the farm.</p>"""
    membership_level: "capo_deadline.types.membership_level.MembershipLevel"
    """<p>The principal's membership level for the associated farm.</p>"""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>The member's principal ID to associate with the farm.</p>"""
    identity_center_region: NotRequired["capo_deadline.types.region.Region"]
    """<p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMemberToFarmRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.deadline_principal_type

    out["principalType"] = capo_deadline.types.deadline_principal_type.serialize_json(
        value["principal_type"]
    )
    out["identityStoreId"] = value["identity_store_id"]
    import capo_deadline.types.membership_level

    out["membershipLevel"] = capo_deadline.types.membership_level.serialize_json(
        value["membership_level"]
    )
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    return out


def deserialize_json(data: dict) -> AssociateMemberToFarmRequest:
    out: AssociateMemberToFarmRequest = {}  # type: ignore[typeddict-item]
    if "principalType" in data:
        import capo_deadline.types.deadline_principal_type

        out["principal_type"] = (
            capo_deadline.types.deadline_principal_type.deserialize_json(
                data["principalType"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateMemberToFarmRequest.principal_type required"
        )
    if "identityStoreId" in data:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        raise DeserializationError(
            "AssociateMemberToFarmRequest.identity_store_id required"
        )
    if "membershipLevel" in data:
        import capo_deadline.types.membership_level

        out["membership_level"] = capo_deadline.types.membership_level.deserialize_json(
            data["membershipLevel"]
        )
    else:
        raise DeserializationError(
            "AssociateMemberToFarmRequest.membership_level required"
        )
    if "identityCenterRegion" in data:
        out["identity_center_region"] = data["identityCenterRegion"]
    return out
