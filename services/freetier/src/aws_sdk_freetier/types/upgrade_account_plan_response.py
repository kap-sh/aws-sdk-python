"""Generated from Smithy shape ``com.amazonaws.freetier#UpgradeAccountPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.account_id
    import aws_sdk_freetier.types.account_plan_status
    import aws_sdk_freetier.types.account_plan_type


class UpgradeAccountPlanResponse(TypedDict, closed=True):
    account_id: "aws_sdk_freetier.types.account_id.AccountId"
    """<p> A unique identifier that identifies the account. </p>"""
    account_plan_type: "aws_sdk_freetier.types.account_plan_type.AccountPlanType"
    """<p> The type of plan for the account. </p>"""
    account_plan_status: "aws_sdk_freetier.types.account_plan_status.AccountPlanStatus"
    """<p> This indicates the latest state of the account plan within its lifecycle. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpgradeAccountPlanResponse) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> UpgradeAccountPlanResponse:
    out: UpgradeAccountPlanResponse = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("UpgradeAccountPlanResponse.account_id required")
    if "accountPlanType" in data:
        import aws_sdk_freetier.types.account_plan_type

        out["account_plan_type"] = (
            aws_sdk_freetier.types.account_plan_type.deserialize_aws_json_1_0(
                data["accountPlanType"]
            )
        )
    else:
        raise DeserializationError(
            "UpgradeAccountPlanResponse.account_plan_type required"
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
            "UpgradeAccountPlanResponse.account_plan_status required"
        )
    return out
