"""Generated from Smithy shape ``com.amazonaws.deadline#AssociateMemberToFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.deadline_principal_type
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.identity_center_principal_id
    import aws_sdk_deadline.types.identity_store_id
    import aws_sdk_deadline.types.membership_level
    import aws_sdk_deadline.types.region


class AssociateMemberToFleetRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the fleet to associate with the member.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The ID of the fleet to associate with a member.</p>"""
    principal_type: (
        "aws_sdk_deadline.types.deadline_principal_type.DeadlinePrincipalType"
    )
    """<p>The member's principal type to associate with the fleet.</p>"""
    identity_store_id: "aws_sdk_deadline.types.identity_store_id.IdentityStoreId"
    """<p>The member's identity store ID to associate with the fleet.</p>"""
    membership_level: "aws_sdk_deadline.types.membership_level.MembershipLevel"
    """<p>The principal's membership level for the associated fleet.</p>"""
    principal_id: (
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>The member's principal ID to associate with a fleet.</p>"""
    identity_center_region: NotRequired["aws_sdk_deadline.types.region.Region"]
    """<p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMemberToFleetRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.deadline_principal_type

    out["principalType"] = (
        aws_sdk_deadline.types.deadline_principal_type.serialize_json(
            value["principal_type"]
        )
    )
    out["identityStoreId"] = value["identity_store_id"]
    import aws_sdk_deadline.types.membership_level

    out["membershipLevel"] = aws_sdk_deadline.types.membership_level.serialize_json(
        value["membership_level"]
    )
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    return out


def deserialize_json(data: dict) -> AssociateMemberToFleetRequest:
    out: AssociateMemberToFleetRequest = {}  # type: ignore[typeddict-item]
    if "principalType" in data:
        import aws_sdk_deadline.types.deadline_principal_type

        out["principal_type"] = (
            aws_sdk_deadline.types.deadline_principal_type.deserialize_json(
                data["principalType"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateMemberToFleetRequest.principal_type required"
        )
    if "identityStoreId" in data:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        raise DeserializationError(
            "AssociateMemberToFleetRequest.identity_store_id required"
        )
    if "membershipLevel" in data:
        import aws_sdk_deadline.types.membership_level

        out["membership_level"] = (
            aws_sdk_deadline.types.membership_level.deserialize_json(
                data["membershipLevel"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateMemberToFleetRequest.membership_level required"
        )
    if "identityCenterRegion" in data:
        out["identity_center_region"] = data["identityCenterRegion"]
    return out
