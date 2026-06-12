"""Generated from Smithy shape ``com.amazonaws.deadline#QueueMember``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.deadline_principal_type
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.identity_center_principal_id
    import aws_sdk_deadline.types.identity_store_id
    import aws_sdk_deadline.types.membership_level
    import aws_sdk_deadline.types.queue_id


class QueueMember(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""
    principal_id: (
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>The principal ID of the queue member.</p>"""
    principal_type: (
        "aws_sdk_deadline.types.deadline_principal_type.DeadlinePrincipalType"
    )
    """<p>The principal type of the queue member.</p>"""
    identity_store_id: "aws_sdk_deadline.types.identity_store_id.IdentityStoreId"
    """<p>The identity store ID.</p>"""
    membership_level: "aws_sdk_deadline.types.membership_level.MembershipLevel"
    """<p>The queue member's membership level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueMember) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["principalId"] = value["principal_id"]
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
    return out


def deserialize_json(data: dict) -> QueueMember:
    out: QueueMember = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("QueueMember.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("QueueMember.queue_id required")
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    else:
        raise DeserializationError("QueueMember.principal_id required")
    if "principalType" in data:
        import aws_sdk_deadline.types.deadline_principal_type

        out["principal_type"] = (
            aws_sdk_deadline.types.deadline_principal_type.deserialize_json(
                data["principalType"]
            )
        )
    else:
        raise DeserializationError("QueueMember.principal_type required")
    if "identityStoreId" in data:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        raise DeserializationError("QueueMember.identity_store_id required")
    if "membershipLevel" in data:
        import aws_sdk_deadline.types.membership_level

        out["membership_level"] = (
            aws_sdk_deadline.types.membership_level.deserialize_json(
                data["membershipLevel"]
            )
        )
    else:
        raise DeserializationError("QueueMember.membership_level required")
    return out
