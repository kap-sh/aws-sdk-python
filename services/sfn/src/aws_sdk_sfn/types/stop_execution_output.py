"""Generated from Smithy shape ``com.amazonaws.sfn#StopExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.timestamp


class StopExecutionOutput(TypedDict):
    stop_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the execution is stopped.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopExecutionOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.timestamp

    out["stopDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["stop_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StopExecutionOutput:
    out: StopExecutionOutput = {}  # type: ignore[typeddict-item]
    if "stopDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["stop_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    else:
        raise DeserializationError("StopExecutionOutput.stop_date required")
    return out
