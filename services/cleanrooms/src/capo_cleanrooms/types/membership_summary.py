"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_payment_configuration
    import capo_cleanrooms.types.membership_status
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.uuid


class MembershipSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership's collaboration.</p>"""
    arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the membership's associated collaboration.</p>"""
    collaboration_id: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique ID for the membership's collaboration.</p>"""
    collaboration_creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier of the Amazon Web Services principal that created the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    collaboration_creator_display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The display name of the collaboration creator.</p>"""
    collaboration_name: "capo_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>The name for the membership's collaboration.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the membership was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the membership metadata was last updated.</p>"""
    status: "capo_cleanrooms.types.membership_status.MembershipStatus"
    """<p>The status of the membership.</p>"""
    member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member.</p>"""
    ml_member_abilities: NotRequired[
        "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>Provides a summary of the ML abilities for the collaboration member.</p>"""
    payment_configuration: "capo_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
    """<p>The payment responsibilities accepted by the collaboration member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationCreatorAccountId"] = value["collaboration_creator_account_id"]
    out["collaborationCreatorDisplayName"] = value["collaboration_creator_display_name"]
    out["collaborationName"] = value["collaboration_name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["status"] = value["status"]
    import capo_cleanrooms.types.member_abilities

    out["memberAbilities"] = capo_cleanrooms.types.member_abilities.serialize_json(
        value["member_abilities"]
    )
    if "ml_member_abilities" in value:
        import capo_cleanrooms.types.ml_member_abilities

        out["mlMemberAbilities"] = (
            capo_cleanrooms.types.ml_member_abilities.serialize_json(
                value["ml_member_abilities"]
            )
        )
    import capo_cleanrooms.types.membership_payment_configuration

    out["paymentConfiguration"] = (
        capo_cleanrooms.types.membership_payment_configuration.serialize_json(
            value["payment_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> MembershipSummary:
    out: MembershipSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("MembershipSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("MembershipSummary.arn required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("MembershipSummary.collaboration_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("MembershipSummary.collaboration_id required")
    if "collaborationCreatorAccountId" in data:
        out["collaboration_creator_account_id"] = data["collaborationCreatorAccountId"]
    else:
        raise DeserializationError(
            "MembershipSummary.collaboration_creator_account_id required"
        )
    if "collaborationCreatorDisplayName" in data:
        out["collaboration_creator_display_name"] = data[
            "collaborationCreatorDisplayName"
        ]
    else:
        raise DeserializationError(
            "MembershipSummary.collaboration_creator_display_name required"
        )
    if "collaborationName" in data:
        out["collaboration_name"] = data["collaborationName"]
    else:
        raise DeserializationError("MembershipSummary.collaboration_name required")
    if "createTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("MembershipSummary.create_time required")
    if "updateTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("MembershipSummary.update_time required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("MembershipSummary.status required")
    if "memberAbilities" in data:
        import capo_cleanrooms.types.member_abilities

        out["member_abilities"] = (
            capo_cleanrooms.types.member_abilities.deserialize_json(
                data["memberAbilities"]
            )
        )
    else:
        raise DeserializationError("MembershipSummary.member_abilities required")
    if "mlMemberAbilities" in data:
        import capo_cleanrooms.types.ml_member_abilities

        out["ml_member_abilities"] = (
            capo_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["mlMemberAbilities"]
            )
        )
    if "paymentConfiguration" in data:
        import capo_cleanrooms.types.membership_payment_configuration

        out["payment_configuration"] = (
            capo_cleanrooms.types.membership_payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    else:
        raise DeserializationError("MembershipSummary.payment_configuration required")
    return out
