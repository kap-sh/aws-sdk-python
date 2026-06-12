"""Generated from Smithy shape ``com.amazonaws.sfn#PublishStateMachineVersionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.timestamp


class PublishStateMachineVersionOutput(TypedDict):
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the version was created.</p>"""
    state_machine_version_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) (ARN) that identifies the state machine version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishStateMachineVersionOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PublishStateMachineVersionOutput:
    out: PublishStateMachineVersionOutput = {}  # type: ignore[typeddict-item]
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError(
            "PublishStateMachineVersionOutput.creation_date required"
        )
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    else:
        raise DeserializationError(
            "PublishStateMachineVersionOutput.state_machine_version_arn required"
        )
    return out
