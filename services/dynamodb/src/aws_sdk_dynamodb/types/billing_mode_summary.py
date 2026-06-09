"""Generated from Smithy shape ``com.amazonaws.dynamodb#BillingModeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.date


class BillingModeSummary(TypedDict):
    billing_mode: NotRequired["aws_sdk_dynamodb.types.billing_mode.BillingMode"]
    """<p>Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.</p> <ul> <li> <p> <code>PROVISIONED</code> - Sets the read/write capacity mode to <code>PROVISIONED</code>. We recommend using <code>PROVISIONED</code> for predictable workloads.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - Sets the read/write capacity mode to <code>PAY_PER_REQUEST</code>. We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. </p> </li> </ul>"""
    last_update_to_pay_per_request_date_time: NotRequired[
        "aws_sdk_dynamodb.types.date.Date"
    ]
    """<p>Represents the time when <code>PAY_PER_REQUEST</code> was last set as the read/write capacity mode.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingModeSummary) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import aws_sdk_dynamodb.types.billing_mode

        out["BillingMode"] = aws_sdk_dynamodb.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    if "last_update_to_pay_per_request_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["LastUpdateToPayPerRequestDateTime"] = (
            aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
                value["last_update_to_pay_per_request_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingModeSummary:
    out: BillingModeSummary = {}  # type: ignore[typeddict-item]
    if "BillingMode" in data:
        import aws_sdk_dynamodb.types.billing_mode

        out["billing_mode"] = (
            aws_sdk_dynamodb.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    if "LastUpdateToPayPerRequestDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["last_update_to_pay_per_request_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["LastUpdateToPayPerRequestDateTime"]
            )
        )
    return out
