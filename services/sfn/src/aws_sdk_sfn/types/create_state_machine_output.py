"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.timestamp


class CreateStateMachineOutput(TypedDict):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the created state machine.</p>"""
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the state machine is created.</p>"""
    state_machine_version_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the created state machine version. If you do not set the <code>publish</code> parameter to <code>true</code>, this field returns null value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineOutput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineOutput:
    out: CreateStateMachineOutput = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError(
            "CreateStateMachineOutput.state_machine_arn required"
        )
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("CreateStateMachineOutput.creation_date required")
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    return out
