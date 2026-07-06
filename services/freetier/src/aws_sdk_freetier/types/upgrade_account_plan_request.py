"""Generated from Smithy shape ``com.amazonaws.freetier#UpgradeAccountPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.account_plan_type


class UpgradeAccountPlanRequest(TypedDict, closed=True):
    account_plan_type: "aws_sdk_freetier.types.account_plan_type.AccountPlanType"
    """<p> The target account plan type. This makes it explicit about the change and latest value of the <code>accountPlanType</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpgradeAccountPlanRequest) -> dict:
    out: dict = {}
    import aws_sdk_freetier.types.account_plan_type

    out["accountPlanType"] = (
        aws_sdk_freetier.types.account_plan_type.serialize_aws_json_1_0(
            value["account_plan_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpgradeAccountPlanRequest:
    out: UpgradeAccountPlanRequest = {}  # type: ignore[typeddict-item]
    if "accountPlanType" in data:
        import aws_sdk_freetier.types.account_plan_type

        out["account_plan_type"] = (
            aws_sdk_freetier.types.account_plan_type.deserialize_aws_json_1_0(
                data["accountPlanType"]
            )
        )
    else:
        raise DeserializationError(
            "UpgradeAccountPlanRequest.account_plan_type required"
        )
    return out
