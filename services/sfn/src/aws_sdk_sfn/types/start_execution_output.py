"""Generated from Smithy shape ``com.amazonaws.sfn#StartExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.timestamp


class StartExecutionOutput(TypedDict):
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution.</p>"""
    start_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the execution is started.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartExecutionOutput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    import aws_sdk_sfn.types.timestamp

    out["startDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartExecutionOutput:
    out: StartExecutionOutput = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("StartExecutionOutput.execution_arn required")
    if "startDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["start_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        raise DeserializationError("StartExecutionOutput.start_date required")
    return out
