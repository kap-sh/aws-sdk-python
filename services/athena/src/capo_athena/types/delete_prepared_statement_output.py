"""Generated from Smithy shape ``com.amazonaws.athena#DeletePreparedStatementOutput``."""

from typing_extensions import TypedDict


class DeletePreparedStatementOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePreparedStatementOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePreparedStatementOutput:
    out: DeletePreparedStatementOutput = {}  # type: ignore[typeddict-item]
    return out
