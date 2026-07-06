"""Generated from Smithy shape ``com.amazonaws.snowball#CancelClusterResult``."""

from typing_extensions import TypedDict


class CancelClusterResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelClusterResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelClusterResult:
    out: CancelClusterResult = {}  # type: ignore[typeddict-item]
    return out
