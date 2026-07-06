"""Generated from Smithy shape ``com.amazonaws.braket#DeleteSpendingLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_braket.types.spending_limit_arn


class DeleteSpendingLimitRequest(TypedDict, closed=True):
    spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn"
    """<p>The Amazon Resource Name (ARN) of the spending limit to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSpendingLimitRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSpendingLimitRequest:
    out: DeleteSpendingLimitRequest = {}  # type: ignore[typeddict-item]
    return out
