"""Generated from Smithy shape ``com.amazonaws.freetier#GetAccountPlanStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_freetier.types.account_id
    import aws_sdk_freetier.types.account_plan_status
    import aws_sdk_freetier.types.account_plan_type
    import aws_sdk_freetier.types.monetary_amount


class GetAccountPlanStateResponse(TypedDict):
    account_id: "aws_sdk_freetier.types.account_id.AccountId"
    """<p> A unique identifier that identifies the account. </p>"""
    account_plan_type: "aws_sdk_freetier.types.account_plan_type.AccountPlanType"
    """<p> The plan type for the account. </p>"""
    account_plan_status: "aws_sdk_freetier.types.account_plan_status.AccountPlanStatus"
    """<p> The current status for the account plan. </p>"""
    account_plan_remaining_credits: NotRequired[
        "aws_sdk_freetier.types.monetary_amount.MonetaryAmount"
    ]
    """<p> The amount of credits remaining for the account. </p>"""
    account_plan_expiration_date: NotRequired["datetime.datetime"]
    """<p> The timestamp for when the current account plan expires. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountPlanStateResponse) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import aws_sdk_freetier.types.account_plan_type

    out["accountPlanType"] = (
        aws_sdk_freetier.types.account_plan_type.serialize_aws_json_1_0(
            value["account_plan_type"]
        )
    )
    import aws_sdk_freetier.types.account_plan_status

    out["accountPlanStatus"] = (
        aws_sdk_freetier.types.account_plan_status.serialize_aws_json_1_0(
            value["account_plan_status"]
        )
    )
    if "account_plan_remaining_credits" in value:
        import aws_sdk_freetier.types.monetary_amount

        out["accountPlanRemainingCredits"] = (
            aws_sdk_freetier.types.monetary_amount.serialize_aws_json_1_0(
                value["account_plan_remaining_credits"]
            )
        )
    if "account_plan_expiration_date" in value:
        import aws_sdk_freetier.types._prelude.timestamp

        out["accountPlanExpirationDate"] = (
            aws_sdk_freetier.types._prelude.timestamp.serialize_aws_json_1_0(
                value["account_plan_expiration_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountPlanStateResponse:
    out: GetAccountPlanStateResponse = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("GetAccountPlanStateResponse.account_id required")
    if "accountPlanType" in data:
        import aws_sdk_freetier.types.account_plan_type

        out["account_plan_type"] = (
            aws_sdk_freetier.types.account_plan_type.deserialize_aws_json_1_0(
                data["accountPlanType"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountPlanStateResponse.account_plan_type required"
        )
    if "accountPlanStatus" in data:
        import aws_sdk_freetier.types.account_plan_status

        out["account_plan_status"] = (
            aws_sdk_freetier.types.account_plan_status.deserialize_aws_json_1_0(
                data["accountPlanStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountPlanStateResponse.account_plan_status required"
        )
    if "accountPlanRemainingCredits" in data:
        import aws_sdk_freetier.types.monetary_amount

        out["account_plan_remaining_credits"] = (
            aws_sdk_freetier.types.monetary_amount.deserialize_aws_json_1_0(
                data["accountPlanRemainingCredits"]
            )
        )
    if "accountPlanExpirationDate" in data:
        import aws_sdk_freetier.types._prelude.timestamp

        out["account_plan_expiration_date"] = (
            aws_sdk_freetier.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["accountPlanExpirationDate"]
            )
        )
    return out
