"""Generated from Smithy shape ``com.amazonaws.sfn#RedriveExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.timestamp


class RedriveExecutionOutput(TypedDict):
    redrive_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the execution was last redriven.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RedriveExecutionOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.timestamp

    out["redriveDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["redrive_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RedriveExecutionOutput:
    out: RedriveExecutionOutput = {}  # type: ignore[typeddict-item]
    if "redriveDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["redrive_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["redriveDate"]
        )
    else:
        raise DeserializationError("RedriveExecutionOutput.redrive_date required")
    return out
