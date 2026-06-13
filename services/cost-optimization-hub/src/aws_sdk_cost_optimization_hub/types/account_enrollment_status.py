"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#AccountEnrollmentStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cost_optimization_hub.types.account_id
    import aws_sdk_cost_optimization_hub.types.enrollment_status


class AccountEnrollmentStatus(TypedDict):
    account_id: NotRequired["aws_sdk_cost_optimization_hub.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    status: NotRequired[
        "aws_sdk_cost_optimization_hub.types.enrollment_status.EnrollmentStatus"
    ]
    """<p>The account enrollment status.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the account enrollment status was last updated.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the account enrollment status was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountEnrollmentStatus) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import aws_sdk_cost_optimization_hub.types.enrollment_status

        out["status"] = (
            aws_sdk_cost_optimization_hub.types.enrollment_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_cost_optimization_hub.types._prelude.timestamp

        out["lastUpdatedTimestamp"] = (
            aws_sdk_cost_optimization_hub.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_cost_optimization_hub.types._prelude.timestamp

        out["createdTimestamp"] = (
            aws_sdk_cost_optimization_hub.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountEnrollmentStatus:
    out: AccountEnrollmentStatus = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        import aws_sdk_cost_optimization_hub.types.enrollment_status

        out["status"] = (
            aws_sdk_cost_optimization_hub.types.enrollment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_cost_optimization_hub.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_cost_optimization_hub.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    if "createdTimestamp" in data:
        import aws_sdk_cost_optimization_hub.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_cost_optimization_hub.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    return out
