"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.timestamp


class MapRunListItem(TypedDict):
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The <code>executionArn</code> of the execution from which the Map Run was started.</p>"""
    map_run_arn: "aws_sdk_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the Map Run.</p>"""
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the executed state machine.</p>"""
    start_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date on which the Map Run started.</p>"""
    stop_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>The date on which the Map Run stopped.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunListItem) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    out["mapRunArn"] = value["map_run_arn"]
    out["stateMachineArn"] = value["state_machine_arn"]
    import aws_sdk_sfn.types.timestamp

    out["startDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "stop_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["stopDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["stop_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MapRunListItem:
    out: MapRunListItem = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("MapRunListItem.execution_arn required")
    if "mapRunArn" in data:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        raise DeserializationError("MapRunListItem.map_run_arn required")
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("MapRunListItem.state_machine_arn required")
    if "startDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["start_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        raise DeserializationError("MapRunListItem.start_date required")
    if "stopDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["stop_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    return out
