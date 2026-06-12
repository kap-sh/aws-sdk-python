"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimestreamConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.iam_role_arn
    import aws_sdk_iotfleetwise.types.timestream_table_arn


class TimestreamConfig(TypedDict):
    timestream_table_arn: (
        "aws_sdk_iotfleetwise.types.timestream_table_arn.TimestreamTableArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Timestream table.</p>"""
    execution_role_arn: "aws_sdk_iotfleetwise.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants Amazon Web Services IoT FleetWise permission to deliver data to the Amazon Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestreamConfig) -> dict:
    out: dict = {}
    out["timestreamTableArn"] = value["timestream_table_arn"]
    out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimestreamConfig:
    out: TimestreamConfig = {}  # type: ignore[typeddict-item]
    if "timestreamTableArn" in data:
        out["timestream_table_arn"] = data["timestreamTableArn"]
    else:
        raise DeserializationError("TimestreamConfig.timestream_table_arn required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("TimestreamConfig.execution_role_arn required")
    return out
