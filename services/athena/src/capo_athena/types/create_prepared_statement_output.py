"""Generated from Smithy shape ``com.amazonaws.athena#CreatePreparedStatementOutput``."""

from typing_extensions import TypedDict


class CreatePreparedStatementOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePreparedStatementOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePreparedStatementOutput:
    out: CreatePreparedStatementOutput = {}  # type: ignore[typeddict-item]
    return out
