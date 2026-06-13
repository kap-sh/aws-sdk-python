"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberChangeSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.member_abilities
    import aws_sdk_cleanrooms.types.ml_member_abilities
    import aws_sdk_cleanrooms.types.payment_configuration


class MemberChangeSpecification(TypedDict):
    account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member to add to the collaboration.</p>"""
    member_abilities: "aws_sdk_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member. These determine what actions the member can perform within the collaboration.</p> <note> <p>The following values are currently not supported: <code>CAN_QUERY</code> and <code>CAN_RUN_JOB</code>. </p> <p>Set the value of <code>memberAbilities</code> to <code>[]</code> to allow a member to contribute data.</p> <p>Set the value of <code>memberAbilities</code> to <code>[CAN_RECEIVE_RESULTS]</code> to allow a member to contribute data and receive results.</p> </note>"""
    ml_member_abilities: NotRequired[
        "aws_sdk_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    payment_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.payment_configuration.PaymentConfiguration"
    ]
    display_name: NotRequired["aws_sdk_cleanrooms.types.display_name.DisplayName"]
    """<p>Specifies the display name that will be shown for this member in the collaboration. While this field is required when inviting new members, it becomes optional when modifying abilities of existing collaboration members. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberChangeSpecification) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import aws_sdk_cleanrooms.types.member_abilities

    out["memberAbilities"] = aws_sdk_cleanrooms.types.member_abilities.serialize_json(
        value["member_abilities"]
    )
    if "ml_member_abilities" in value:
        import aws_sdk_cleanrooms.types.ml_member_abilities

        out["mlMemberAbilities"] = (
            aws_sdk_cleanrooms.types.ml_member_abilities.serialize_json(
                value["ml_member_abilities"]
            )
        )
    if "payment_configuration" in value:
        import aws_sdk_cleanrooms.types.payment_configuration

        out["paymentConfiguration"] = (
            aws_sdk_cleanrooms.types.payment_configuration.serialize_json(
                value["payment_configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> MemberChangeSpecification:
    out: MemberChangeSpecification = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("MemberChangeSpecification.account_id required")
    if "memberAbilities" in data:
        import aws_sdk_cleanrooms.types.member_abilities

        out["member_abilities"] = (
            aws_sdk_cleanrooms.types.member_abilities.deserialize_json(
                data["memberAbilities"]
            )
        )
    else:
        raise DeserializationError(
            "MemberChangeSpecification.member_abilities required"
        )
    if "mlMemberAbilities" in data:
        import aws_sdk_cleanrooms.types.ml_member_abilities

        out["ml_member_abilities"] = (
            aws_sdk_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["mlMemberAbilities"]
            )
        )
    if "paymentConfiguration" in data:
        import aws_sdk_cleanrooms.types.payment_configuration

        out["payment_configuration"] = (
            aws_sdk_cleanrooms.types.payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
