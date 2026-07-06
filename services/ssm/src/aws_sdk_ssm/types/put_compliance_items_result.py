"""Generated from Smithy shape ``com.amazonaws.ssm#PutComplianceItemsResult``."""

from typing_extensions import TypedDict


class PutComplianceItemsResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutComplianceItemsResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutComplianceItemsResult:
    out: PutComplianceItemsResult = {}  # type: ignore[typeddict-item]
    return out
