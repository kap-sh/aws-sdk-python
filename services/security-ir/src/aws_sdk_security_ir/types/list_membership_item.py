"""Generated from Smithy shape ``com.amazonaws.securityir#ListMembershipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_account_id
    import aws_sdk_security_ir.types.aws_region
    import aws_sdk_security_ir.types.membership_arn
    import aws_sdk_security_ir.types.membership_id
    import aws_sdk_security_ir.types.membership_status


class ListMembershipItem(TypedDict, closed=True):
    membership_id: "aws_sdk_security_ir.types.membership_id.MembershipId"
    """<p/>"""
    account_id: NotRequired["aws_sdk_security_ir.types.aws_account_id.AWSAccountId"]
    """<p/>"""
    region: NotRequired["aws_sdk_security_ir.types.aws_region.AwsRegion"]
    """<p/>"""
    membership_arn: NotRequired[
        "aws_sdk_security_ir.types.membership_arn.MembershipArn"
    ]
    """<p/>"""
    membership_status: NotRequired[
        "aws_sdk_security_ir.types.membership_status.MembershipStatus"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipItem) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        import aws_sdk_security_ir.types.aws_region

        out["region"] = aws_sdk_security_ir.types.aws_region.serialize_json(
            value["region"]
        )
    if "membership_arn" in value:
        out["membershipArn"] = value["membership_arn"]
    if "membership_status" in value:
        import aws_sdk_security_ir.types.membership_status

        out["membershipStatus"] = (
            aws_sdk_security_ir.types.membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMembershipItem:
    out: ListMembershipItem = {}  # type: ignore[typeddict-item]
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ListMembershipItem.membership_id required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "region" in data:
        import aws_sdk_security_ir.types.aws_region

        out["region"] = aws_sdk_security_ir.types.aws_region.deserialize_json(
            data["region"]
        )
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    if "membershipStatus" in data:
        import aws_sdk_security_ir.types.membership_status

        out["membership_status"] = (
            aws_sdk_security_ir.types.membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out
