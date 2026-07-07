"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteAnomalySubscriptionResponse``."""

from typing_extensions import TypedDict


class DeleteAnomalySubscriptionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAnomalySubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAnomalySubscriptionResponse:
    out: DeleteAnomalySubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out
