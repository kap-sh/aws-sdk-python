"""Generated from Smithy shape ``com.amazonaws.glue#CancelStatementResponse``."""

from typing_extensions import TypedDict


class CancelStatementResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStatementResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelStatementResponse:
    out: CancelStatementResponse = {}  # type: ignore[typeddict-item]
    return out
