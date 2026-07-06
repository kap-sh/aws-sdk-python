"""Generated from Smithy shape ``com.amazonaws.mturk#GetAccountBalanceRequest``."""

from typing_extensions import TypedDict


class GetAccountBalanceRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountBalanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountBalanceRequest:
    out: GetAccountBalanceRequest = {}  # type: ignore[typeddict-item]
    return out
