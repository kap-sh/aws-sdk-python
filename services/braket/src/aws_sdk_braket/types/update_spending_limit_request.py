"""Generated from Smithy shape ``com.amazonaws.braket#UpdateSpendingLimitRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.spending_limit_arn
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.time_period


class UpdateSpendingLimitRequest(TypedDict):
    spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn"
    """<p>The Amazon Resource Name (ARN) of the spending limit to update.</p>"""
    client_token: "aws_sdk_braket.types.string64.String64"
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>"""
    spending_limit: NotRequired["str"]
    """<p>The new maximum amount that can be spent on the specified device, in USD.</p>"""
    time_period: NotRequired["aws_sdk_braket.types.time_period.TimePeriod"]
    """<p>The new time period during which the spending limit is active, including start and end dates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpendingLimitRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    if "spending_limit" in value:
        out["spendingLimit"] = value["spending_limit"]
    if "time_period" in value:
        import aws_sdk_braket.types.time_period

        out["timePeriod"] = aws_sdk_braket.types.time_period.serialize_json(
            value["time_period"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSpendingLimitRequest:
    out: UpdateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateSpendingLimitRequest.client_token required")
    if "spendingLimit" in data:
        out["spending_limit"] = data["spendingLimit"]
    if "timePeriod" in data:
        import aws_sdk_braket.types.time_period

        out["time_period"] = aws_sdk_braket.types.time_period.deserialize_json(
            data["timePeriod"]
        )
    return out
