"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.execution_status
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.redrive_count
    import aws_sdk_sfn.types.timestamp
    import aws_sdk_sfn.types.unsigned_integer


class ExecutionListItem(TypedDict):
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution.</p>"""
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine that ran the execution.</p>"""
    name: "aws_sdk_sfn.types.name.Name"
    """<p>The name of the execution.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>\" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    status: "aws_sdk_sfn.types.execution_status.ExecutionStatus"
    """<p>The current status of the execution.</p>"""
    start_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the execution started.</p>"""
    stop_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>If the execution already ended, the date the execution stopped.</p>"""
    map_run_arn: NotRequired["aws_sdk_sfn.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of a Map Run. This field is returned only if <code>mapRunArn</code> was specified in the <code>ListExecutions</code> API action. If <code>stateMachineArn</code> was specified in <code>ListExecutions</code>, the <code>mapRunArn</code> isn't returned.</p>"""
    item_count: NotRequired["aws_sdk_sfn.types.unsigned_integer.UnsignedInteger"]
    """<p>The total number of items processed in a child workflow execution. This field is returned only if <code>mapRunArn</code> was specified in the <code>ListExecutions</code> API action. If <code>stateMachineArn</code> was specified in <code>ListExecutions</code>, the <code>itemCount</code> field isn't returned.</p>"""
    state_machine_version_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine version associated with the execution.</p> <p>If the state machine execution was started with an unqualified ARN, it returns null.</p> <p>If the execution was started using a <code>stateMachineAliasArn</code>, both the <code>stateMachineAliasArn</code> and <code>stateMachineVersionArn</code> parameters contain the respective values.</p>"""
    state_machine_alias_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine alias used to start an execution.</p> <p>If the state machine execution was started with an unqualified ARN or a version ARN, it returns null.</p>"""
    redrive_count: NotRequired["aws_sdk_sfn.types.redrive_count.RedriveCount"]
    """<p>The number of times you've redriven an execution. If you have not yet redriven an execution, the <code>redriveCount</code> is 0. This count is only updated when you successfully redrive an execution.</p>"""
    redrive_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>The date the execution was last redriven.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionListItem) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    out["stateMachineArn"] = value["state_machine_arn"]
    out["name"] = value["name"]
    import aws_sdk_sfn.types.execution_status

    out["status"] = aws_sdk_sfn.types.execution_status.serialize_aws_json_1_0(
        value["status"]
    )
    import aws_sdk_sfn.types.timestamp

    out["startDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "stop_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["stopDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["stop_date"]
        )
    if "map_run_arn" in value:
        out["mapRunArn"] = value["map_run_arn"]
    if "item_count" in value:
        out["itemCount"] = value["item_count"]
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    if "state_machine_alias_arn" in value:
        out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "redrive_count" in value:
        out["redriveCount"] = value["redrive_count"]
    if "redrive_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["redriveDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["redrive_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionListItem:
    out: ExecutionListItem = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("ExecutionListItem.execution_arn required")
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("ExecutionListItem.state_machine_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ExecutionListItem.name required")
    if "status" in data:
        import aws_sdk_sfn.types.execution_status

        out["status"] = aws_sdk_sfn.types.execution_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("ExecutionListItem.status required")
    if "startDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["start_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        raise DeserializationError("ExecutionListItem.start_date required")
    if "stopDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["stop_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    if "mapRunArn" in data:
        out["map_run_arn"] = data["mapRunArn"]
    if "itemCount" in data:
        out["item_count"] = data["itemCount"]
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    if "stateMachineAliasArn" in data:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    if "redriveCount" in data:
        out["redrive_count"] = data["redriveCount"]
    if "redriveDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["redrive_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["redriveDate"]
        )
    return out
