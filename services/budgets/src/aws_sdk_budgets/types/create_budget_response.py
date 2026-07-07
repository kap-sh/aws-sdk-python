"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudgetResponse``."""

from typing_extensions import TypedDict


class CreateBudgetResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBudgetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBudgetResponse:
    out: CreateBudgetResponse = {}  # type: ignore[typeddict-item]
    return out
