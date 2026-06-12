"""Generated from Smithy shape ``com.amazonaws.mturk#ListBonusPaymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.bonus_payment_list
    import aws_sdk_mturk.types.integer
    import aws_sdk_mturk.types.pagination_token


class ListBonusPaymentsResponse(TypedDict):
    num_results: NotRequired["aws_sdk_mturk.types.integer.Integer"]
    """<p>The number of bonus payments on this page in the filtered results list, equivalent to the number of bonus payments being returned by this call. </p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    bonus_payments: NotRequired[
        "aws_sdk_mturk.types.bonus_payment_list.BonusPaymentList"
    ]
    """<p>A successful request to the ListBonusPayments operation returns a list of BonusPayment objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBonusPaymentsResponse) -> dict:
    out: dict = {}
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "bonus_payments" in value:
        import aws_sdk_mturk.types.bonus_payment_list

        out["BonusPayments"] = (
            aws_sdk_mturk.types.bonus_payment_list.serialize_aws_json_1_1(
                value["bonus_payments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBonusPaymentsResponse:
    out: ListBonusPaymentsResponse = {}  # type: ignore[typeddict-item]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "BonusPayments" in data:
        import aws_sdk_mturk.types.bonus_payment_list

        out["bonus_payments"] = (
            aws_sdk_mturk.types.bonus_payment_list.deserialize_aws_json_1_1(
                data["BonusPayments"]
            )
        )
    return out
