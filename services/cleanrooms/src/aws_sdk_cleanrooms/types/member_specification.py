"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.member_abilities
    import aws_sdk_cleanrooms.types.ml_member_abilities
    import aws_sdk_cleanrooms.types.payment_configuration


class MemberSpecification(TypedDict, closed=True):
    account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    member_abilities: "aws_sdk_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member.</p>"""
    ml_member_abilities: NotRequired[
        "aws_sdk_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>The ML abilities granted to the collaboration member.</p>"""
    display_name: "aws_sdk_cleanrooms.types.display_name.DisplayName"
    """<p>The member's display name.</p>"""
    payment_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.payment_configuration.PaymentConfiguration"
    ]
    """<p>The collaboration member's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't speciﬁed anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberSpecification) -> dict:
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
    out["displayName"] = value["display_name"]
    if "payment_configuration" in value:
        import aws_sdk_cleanrooms.types.payment_configuration

        out["paymentConfiguration"] = (
            aws_sdk_cleanrooms.types.payment_configuration.serialize_json(
                value["payment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberSpecification:
    out: MemberSpecification = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("MemberSpecification.account_id required")
    if "memberAbilities" in data:
        import aws_sdk_cleanrooms.types.member_abilities

        out["member_abilities"] = (
            aws_sdk_cleanrooms.types.member_abilities.deserialize_json(
                data["memberAbilities"]
            )
        )
    else:
        raise DeserializationError("MemberSpecification.member_abilities required")
    if "mlMemberAbilities" in data:
        import aws_sdk_cleanrooms.types.ml_member_abilities

        out["ml_member_abilities"] = (
            aws_sdk_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["mlMemberAbilities"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("MemberSpecification.display_name required")
    if "paymentConfiguration" in data:
        import aws_sdk_cleanrooms.types.payment_configuration

        out["payment_configuration"] = (
            aws_sdk_cleanrooms.types.payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    return out
